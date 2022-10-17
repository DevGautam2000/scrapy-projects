import scrapy
from scrapy.http import FormRequest


# class Payload:
#     def __init__(self, VS, VSG, EV):
#         self.LASTFOCUS = ""
#         self.EVENTTARGET = ""
#         self.EVENTARGUMENT = ""
#         self.VIEWSTATE = VS
#         self.VIEWSTATEGENERATOR = VSG
#         self.EVENTVALIDATION: EV
#         self.tbEmail = ""
#         self.TxtUserName = "201900099"
#         self.TxtPassword = "000992019"
#         self.btnLogin = "Signin"


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['ecm.smtech.in']
    start_urls = ['https://ecm.smtech.in/ecm/login.aspx']

    def parse(self, response):
        user = getattr(self, 'username', '')
        passw = getattr(self, 'password', '')

        def get_data(ID):
            return response.xpath(f"//*[@id='{ID}']/@value").extract()[0]

        VS = get_data("__VIEWSTATE")
        VSG = get_data("__VIEWSTATEGENERATOR")
        EV = get_data("__EVENTVALIDATION")

        yield FormRequest(
            url=self.start_urls[0],
            formdata={
                '__VIEWSTATE': VS,
                '__VIEWSTATEGENERATOR': VSG,
                '__EVENTVALIDATION': EV,
                'TxtUserName': user,
                'TxtPassword': passw,
                'btnLogin': "Signin"
            },
            callback=self.validate
        )

    def validate(self, response):
        if response.xpath("//*[@id='ctl00_lnkSignOut']"):
            name = response.xpath("//*[@id='ctl00_ContentPlaceHolder1_lblName']/text()").extract()[0]
            tg = response.xpath("//*[@id='ctl00_ContentPlaceHolder1_lblTg']/text()").extract()[0]
            self.log({name,tg})
