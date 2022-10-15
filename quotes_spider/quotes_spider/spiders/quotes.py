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

        yield {'header':header,'tags':tags}