from scrapy import Spider, Request
from ..items import ImageItem

class ImageSpider(Spider):
    name = 'image_spider'
    max_page = 1000
    template_url = 'https://danbooru.donmai.us/posts?page={page}&tags={tag}'

    def __init__(self, tags):
        self.tags = tags

    def start_requests(self):
        for tag in self.tags:
            for page in range(1, self.max_page+1):
                yield Request(self.template_url.format(page=page, tag=tag))

    def parse(self, response):
        parent_xpath = './/div[@id="posts-container"]//img'
        items = response.xpath(parent_xpath)

        url_xpath = './@src'
        image_urls = [image for item in items if (image := item.xpath(url_xpath).get(default=None))]

        image_item = ImageItem(image_urls=image_urls)
        return image_item
