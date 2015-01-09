from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from etymonline_scraper.items import Etymology

class EtymonlineSpider(CrawlSpider):
    name = "etymonline.com"
    allowed_domains = ["etymonline.com",
                       "www.etymonline.com"
    ]
    start_urls = ["http://www.etymonline.com/index.php"]
    rules = [Rule(SgmlLinkExtractor(allow=()), "parse_entry", follow=True)]

    def parse_entry(self, response):
        sel = HtmlXPathSelector(response)

        all_dt = sel.xpath('//dt')

        results = []

        for dt in all_dt:
            entry = Etymology()
            entry['word'] = dt.xpath('.//a[1]/text()').extract()
            entry['origin'] = dt.xpath('./following-sibling::dd[1]//text()').extract()

            results.append(entry)

        return results

