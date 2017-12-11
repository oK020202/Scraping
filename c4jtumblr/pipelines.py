# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class C4JtumblrPipeline(object):
    def process_item(self, item, spider):
        # replace image src to downloaded image path
        for image in item['images']:
            print('replace ' + image['url'] + ' to /images/' + image['path'])
            item['post_content'] = item['post_content'].replace(image['url'], '/images/' + image['path'])
        return item 