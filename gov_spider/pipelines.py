# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class GovSpiderPipeline:
    def process_item(self, item, spider):
        return item

    def __init__(self):
        self.file = open("wjbfb.txt", "w")

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()