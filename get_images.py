from web_crawler.spiders.image_spider import ImageSpider
from web_crawler.crawler import Crawler

def get_images(tags):
    crawler = Crawler()
    crawler.run(ImageSpider, tags)

if __name__ == '__main__':
    get_images(
        [
            'blue_eyes',
            'brown_eyes',
            'smile',
            'brown_hair',
            'long_hair',
            'short_hair',
            'black_hair',
            'red_eyes',
            'blonde_hair',
            'white_hair',
            'yellow_eyes',
            'black_eyes',
            'shirt',
            'short_sleeves'
        ]
    )
