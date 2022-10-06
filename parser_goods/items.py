# Define here the models for your scraped items

import scrapy
from itemloaders.processors import MapCompose, TakeFirst


class ParserGoodsItem(scrapy.Item):
    name = scrapy.Field(output_processor=TakeFirst())
    price = scrapy.Field(output_processor=TakeFirst())
    link = scrapy.Field(output_processor=TakeFirst())
    images = scrapy.Field()
    product_description_keys = scrapy.Field(input_processor=MapCompose(lambda x: x.strip()))
    product_description_values = scrapy.Field(input_processor=MapCompose(lambda x: x.strip()))
    product_description = scrapy.Field()
    _id = scrapy.Field()

