Code for Japan の旧Website (http://archive.code4japan.org/) 内の記事を読み込み、WordPressからインポートできる形式のCSVファイルを生成するプログラムです。
ウェブサイトのトップページから各記事のページを開き、その記事の必要な部分のみを読み込み、日付やタイトルの入った、全記事のCSVファイルを生成します。
また、記事からリンクされているイメージ画像も自動的にダウンロードし、本文のimgタグのsrc部分も新しい画像の名前で書き換えます。

| ⚠️ This repository has been archived and will no longer be maintained. Thanks for all the stars, help and brainstorms! |

## 出力ファイルの構成

out/export.csv --- 全記事のCSVファイルです。WordPress のCSVインポート機能の項目になっています。
out/images/full --- スクレイピングして取ってきた画像ファイルが出力されます。ファイル名は、画像のあるURLをSHA1ハッシュ化した名前になっています。

## HOW TO USE
Python 2.7.12 で動くことを確認しています。

このプログラムは scrapy というフレームワークを使っているので、scrapy をインストールしてください。

```
% pip install scrapy
```

本リポジトリをクローンしてください。

```
% git clone https://github.com/codeforjapan/scrape_c4j_tumblr.git
```

ディレクトリに移動して、クロールのコマンドを実行します。

```
% cd scrape_c4j_tumblr
% scrapy crawl c4j
```

色々表示されますが、エラーがでなければOKです。
out ディレクトリ内にエクスポート結果が出力されます。
export.csv が該当のCSVファイルで、images 以下には、記事内の画像が出力されます。

```
ls out
export.csv  images
```

## LICENSE
This software is released under the MIT License, see LICENSE.txt.

