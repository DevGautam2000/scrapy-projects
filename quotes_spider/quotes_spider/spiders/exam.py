import scrapy


class ExamSpider(scrapy.Spider):
    name = 'exam'
    allowed_domains = ['exam.com']
    start_urls = ['http://exam.com/']

    def parse(self, response):
        pass
