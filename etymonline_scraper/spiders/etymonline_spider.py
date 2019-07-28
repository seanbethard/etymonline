from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from etymonline_scraper.items import Etymology

class EtymonlineSpider(CrawlSpider):
    name = "etymonline.com"
    allowed_domains = ["etymonline.com",
                       "www.etymonline.com"
    ]
    start_urls = ["http://www.etymonline.com/index.php"]
    rules = [Rule(LinkExtractor(allow=()), "parse_entry", follow=True)]

    def parse_entry(self, response):
        sel = Selector(response)

        all_dt = sel.xpath('//dt')

        results = []

        for dt in all_dt:
            entry = Etymology()
            entry['word'] = dt.xpath('.//a[1]/text()').extract()
            entry['origin'] = dt.xpath('./following-sibling::dd[1]//text()').extract()

            results.append(entry)

        return results

