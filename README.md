Online Etymology Dictionary Scraper
===================================

It works! I have plans for building an HMM capable of recognizing language of origin from a word's orthographical form.

After you have scrapy installed you can run it with the following command while in the project directory. This will create a large JSON file of word and origins pairs.

  scrapy crawl etymonline.com -o etymonline_data.json -t json
