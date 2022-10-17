import scrapy
from scrapy.http import FormRequest


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/login']

    def parse(self, response):
        csrf_token = response.xpath("//*[@name='csrf_token']/@value").extract_first()
        yield FormRequest(
            url=self.start_urls[0],
            formdata={
                'csrf_token': csrf_token,
                'username': "username",
                'password': "password"
            },
            callback=self.validate)

    def validate(self, response):
        logout = response.xpath("//a[text()='Logout']")
        if logout:
            self.log("YOU LOGGED IN")

