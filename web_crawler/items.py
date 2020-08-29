from scrapy import Item, Field

class ImageItem(Item):
    image_urls = Field()
