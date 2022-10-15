import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def getData(self,xpath,res):
        return res.xpath(f"{xpath}/text()").extract()
    
    def parse(self, response):
        
        header = self.getData(
            xpath="//h1/a",
            res=response)[0];

        tags = self.getData(
            xpath="//*[@class='tag-item']/a",
            res=response);

        quotes = response.xpath('//*[@class="quote"]')

        for quote in quotes:
            yield {
                'quote': quote.xpath(".//span/text()")[0].extract(),
                'author': quote.xpath(".//*[@class='author']/text()").extract_first(),
                'tags': quote.xpath(".//*[@class='tag']/text()").extract()
                }


        next_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        next_page = response.urljoin(next_url)
        
        yield scrapy.Request(next_page)