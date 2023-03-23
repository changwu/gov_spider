import scrapy
from scrapy.selector import Selector
from bs4 import BeautifulSoup
import requests

from gov_spider.items import GovSpiderItem


class WjbfbSpider(scrapy.Spider):
    name = "wjbfb"
    allowed_domains = ["www.scio.gov.cn"]
    start_urls = ["http://www.scio.gov.cn/xwfbh/gbwxwfbh/xwfbh/wjb/index.htm"]

    def parse_content(self, url):
        headers = { 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36' }
        response = requests.get(url, headers=headers)
        html = response.content.decode('utf-8') 
        soup = BeautifulSoup(html, 'lxml')
        title = soup.select('div.tc.A_title')[0].get_text()
        content = soup.select('#content')[0].get_text()
        longstr = soup.select('div.tc.A_t1.f12.pr')[0].get_text()
        arry = longstr.split('\u3000')
        return GovSpiderItem(title=title, content=content, pub_time=arry[3], author=arry[0].strip(), url=url)
        


    def parse(self, response):
        # print(response.text)
        div_list = response.css('div.fl.list_t').extract()
        for div in div_list:
            href = Selector(text=div).css('a::attr(href)').extract_first()
            href = response.urljoin(href)
            print(href)
            yield self.parse_content(href)

        next_url = response.css('#PagerOutline1_PageNext a::attr(href)').extract_first()

        if next_url:
            next_url = response.urljoin(next_url)
            yield scrapy.Request(next_url)

