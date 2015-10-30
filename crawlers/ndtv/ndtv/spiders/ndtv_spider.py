from scrapy.contrib.spiders import Rule,CrawlSpider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.linkextractors import LinkExtractor
from ndtv.items import NdtvItem


class NdtvNewsSpider(CrawlSpider):
    name = "ndtvspider"
    allowed_domains = ["ndtv.com"]
    start_urls = [
            "http://www.ndtv.com/",
    ]
    rules = [Rule(SgmlLinkExtractor(allow=[r"india-news/page-\d*"]), callback="india_news_parser", follow=True),Rule(SgmlLinkExtractor(allow=[r"/india-news\?pfrom=home-topnavigation2015\d*"]), callback="india_news_parser", follow=True),
            Rule(SgmlLinkExtractor(allow=[r"world-news/page-\d*"]), callback="world_news_parser", follow=True),Rule(SgmlLinkExtractor(allow=[r"/world-news\?pfrom=home-topnavigation2015\d*"]), callback="world_news_parser", follow=True),
            Rule(SgmlLinkExtractor(allow=[r"offbeat/page-\d*"]), callback="offbeat_news_parser", follow=True),Rule(SgmlLinkExtractor(allow=[r"/offbeat\?pfrom=home-topnavigation2015\d*"]), callback="offbeat_news_parser", follow=True),
            Rule(SgmlLinkExtractor(allow=[r"latest/page-\d*"]), callback="latest_news_parser", follow=True),Rule(SgmlLinkExtractor(allow=[r"/latest\?pfrom=home-topnavigation2015\d*"]), callback="latest_news_parser", follow=True),
            Rule(SgmlLinkExtractor(allow=[r"health/page-\d*"]), callback="health_news_parser", follow=True),Rule(SgmlLinkExtractor(allow=[r"/health\?pfrom=home-topnavigation2015\d*"]), callback="health_news_parser", follow=True),




            ]
    #rules = (Rule(LinkExtractor(allow="ndtv.com/india-news/"), callback="news_parser", follow=True),)

    def india_news_parser(self,response):
        item = NdtvItem()
        self.log = ("crawling_site:"+response.url)
        print self.log

        content_news = response.xpath('//div[@class = "new_storylising"]/ul/li')
        for individual_news in content_news:
            item = NdtvItem()
            item["image"] = individual_news.xpath('div[@class = "new_storylising_img"]/a/img/@src').extract()[0]
            item["url"] = individual_news.xpath('div[@class = "new_storylising_contentwrap"]/div[@class = "nstory_header"]/a/@href').extract()[0]
            item ["title"] = individual_news.xpath('div[@class = "new_storylising_contentwrap"]/div[@class = "nstory_header"]/a/text()').extract()[0]
            item ["description"] = individual_news.xpath('div[@class = "new_storylising_contentwrap"]/div[@class = "nstory_intro"]/text()').extract()[0]
            item["place"] =  "INDIA"
            item["date"] =  individual_news.xpath('div[@class = "new_storylising_contentwrap"]/div[@class = "nstory_dateline"]').re(r'</a>.*?\|(.*)?')[0]
            item["genre"] = "None"

            yield item 
    
    def world_news_parser(self,response):
        item = NdtvItem()
        self.log = ("crawling_site:"+response.url)
        print self.log

        content_news = response.xpath('//div[@class = "new_storylising"]/ul/li')
        for individual_news in content_news:
            item = NdtvItem()
            item["image"] = individual_news.xpath('div[@class = "new_storylising_img"]/a/img/@src').extract()[0]
            item["url"] = individual_news.xpath('div[@class = "new_storylising_contentwrap"]/div[@class = "nstory_header"]/a/@href').extract()[0]
            item ["title"] = individual_news.xpath('div[@class = "new_storylising_contentwrap"]/div[@class = "nstory_header"]/a/text()').extract()[0]
            item ["description"] = individual_news.xpath('div[@class = "new_storylising_contentwrap"]/div[@class = "nstory_intro"]/text()').extract()[0]
            temp =  individual_news.xpath('div[@class = "new_storylising_contentwrap"]/div[@class = "nstory_dateline"]').re(r'</a>.*?\|(.*)?')[0].split(',')
            item["date"] = (" ").join(temp[0:1])
            item["place"] =  (" ").join(temp[2:])
            item["genre"] = "None"

            yield item


    def offbeat_news_parser(self,response):
        item = NdtvItem()
        self.log = ("crawling_site:"+response.url)
        print self.log

        content_news = response.xpath('//div[@class = "new_storylising"]/ul/li')
        for individual_news in content_news:
            item = NdtvItem()
            item["image"] = individual_news.xpath('div[@class = "new_storylising_img"]/a/img/@src').extract()[0]
            item["url"] = individual_news.xpath('div[@class = "new_storylising_contentwrap"]/div[@class = "nstory_header"]/a/@href').extract()[0]
            item ["title"] = individual_news.xpath('div[@class = "new_storylising_contentwrap"]/div[@class = "nstory_header"]/a/text()').extract()[0]
            item ["description"] = individual_news.xpath('div[@class = "new_storylising_contentwrap"]/div[@class = "nstory_intro"]/text()').extract()[0]
            item["place"] =  "INDIA AND WORLD"
            item["date"] =  individual_news.xpath('div[@class = "new_storylising_contentwrap"]/div[@class = "nstory_dateline"]').re(r'</a>.*?\|(.*)?')[0]
            item["genre"] = "offbeat"

            yield item

    def latest_news_parser(self,response):
        item = NdtvItem()
        self.log = ("crawling_site:"+response.url)
        print self.log

        content_news = response.xpath('//div[@class = "new_storylising"]/ul/li')
        for individual_news in content_news:
            item = NdtvItem()
            item["image"] = individual_news.xpath('div[@class = "new_storylising_img"]/a/img/@src').extract()[0]
            item["url"] = individual_news.xpath('div[@class = "new_storylising_contentwrap"]/div[@class = "nstory_header"]/a/@href').extract()[0]
            item ["title"] = individual_news.xpath('div[@class = "new_storylising_contentwrap"]/div[@class = "nstory_header"]/a/text()').extract()[0]
            item ["description"] = individual_news.xpath('div[@class = "new_storylising_contentwrap"]/div[@class = "nstory_intro"]/text()').extract()[0]
            item["place"] =  "INDIA AND WORLD"
            item["date"] =  individual_news.xpath('div[@class = "new_storylising_contentwrap"]/div[@class = "nstory_dateline"]').re(r'</a>.*?\|(.*)?')[0]
            item["genre"] = "latest"

            yield item

    
    def health_news_parser(self,response):
        item = NdtvItem()
        self.log = ("crawling_site:"+response.url)
        print self.log

        content_news = response.xpath('//div[@class = "new_storylising"]/ul/li')
        for individual_news in content_news:
            item = NdtvItem()
            item["image"] = individual_news.xpath('div[@class = "new_storylising_img"]/a/img/@src').extract()[0]
            item["url"] = individual_news.xpath('div[@class = "new_storylising_contentwrap"]/div[@class = "nstory_header"]/a/@href').extract()[0]
            item ["title"] = individual_news.xpath('div[@class = "new_storylising_contentwrap"]/div[@class = "nstory_header"]/a/text()').extract()[0]
            item ["description"] = individual_news.xpath('div[@class = "new_storylising_contentwrap"]/div[@class = "nstory_intro"]/text()').extract()[0]
            item["place"] =  "INDIA AND WORLD"
            item["date"] =  individual_news.xpath('div[@class = "new_storylising_contentwrap"]/div[@class = "nstory_dateline"]').re(r'</a>.*?\|(.*)?')[0]
            item["genre"] = "health"

            yield item
