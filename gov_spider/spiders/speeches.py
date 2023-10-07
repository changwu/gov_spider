import scrapy

class SpeechesSpider(scrapy.Spider):
    name = 'speeches'
    start_urls = ['https://www.presidency.ucsb.edu/advanced-search?field-keywords=&field-keywords2=&field-keywords3=&from%5Bdate%5D=&to%5Bdate%5D=&person2=&items_per_page=100&page=1']
    base_url = 'https://www.presidency.ucsb.edu'

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse)

    def parse(self, response):
        speech_links = response.css('.views-field-title a::attr(href)').getall()
        for link in speech_links:
            speech_url = self.base_url + link
            yield scrapy.Request(url=speech_url, callback=self.parse_speech)

        # 提取下一页链接并发送请求
        next_page_url = response.css('.next a::attr(href)').get()
        if next_page_url:
            next_page_url = self.base_url + next_page_url
            yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_speech(self, response):
        diet_title = response.css('h3.diet-title').css('::text').get().strip()
        speech_title = response.css('.field-ds-doc-title').css('::text')[1].get().strip()
        docs_date = response.css('.field-docs-start-date-time').css('::text')[1].get().strip()
        texts = response.css('.field-docs-content').css('::text').extract()
        speech_text = ''.join(texts)

        # 保存正文到txt文件
        file_name = f"./speeches/{docs_date} -- {diet_title} -- {speech_title}.txt"

        print(file_name)
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(speech_text)
        self.log(f"保存文件: {file_name}")