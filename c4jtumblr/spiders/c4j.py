# coding: utf-8

from datetime import datetime

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

from c4jtumblr.items import NewsItem


class C4jSpider(CrawlSpider):
    name = 'c4j'
    allowed_domains = ['archive.code4japan.org']
    start_urls = [
        'http://archive.code4japan.org/',
    ]
    def parse(self, response):
        for article in response.css('article'):
            article_page = article.css('.text a::attr("href")').extract_first() 
            if article_page == None:
                article_page = article.css('.photo-hover a::attr("href")').extract_first()
            print(article_page)
            yield response.follow(article_page, self.parse_news)
            
        next_page = response.css('#pagination a#older::attr("href")').extract_first()
        
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def parse_news(self, response):
        item = NewsItem()
        sel = Selector(response)
        article = response.css("article")
        item['article_id'] = article.css("::attr(id)").extract_first()
        item['post_id'] = ""
        item['post_date'] = article.css("::attr(date)").extract_first()
        item['post_name'] = response.url.split("/")[-1]
        item['post_title'] = article.css("div.text h2::text").extract_first()
        item['post_author'] = 'hal'
        item['post_type'] = 'story'
        item['post_status'] = 'draft'
        item['post_category'] = ""
        item['post_tags'] = " ".join(article.css("a.tag::text").extract())
        if item['post_title'] == None:
            item['post_title'] = article.css('div.captions p ::text').extract_first()
        item['post_content'] = article.css('div.text').extract_first()
        if (item['post_content']) == None:
            item['post_content'] = article.css('.photo').extract_first() + article.css('div.text-post div.captions').extract_first()
            
        item['image_urls'] = article.css('img::attr("src")').extract()
        
        yield item