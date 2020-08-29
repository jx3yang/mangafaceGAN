from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

import os

SETTINGS_FILE_PATH = 'web_crawler.settings'

class Crawler(object):
    def __init__(self):
        self.setup()

    def setup(self):
        os.environ.setdefault('SCRAPY_SETTINGS_MODULE', SETTINGS_FILE_PATH)

    def run(self, SpiderClass, *args):
        settings = get_project_settings()

        process = CrawlerProcess(settings)
        process.crawl(SpiderClass, *args)
        process.start()
