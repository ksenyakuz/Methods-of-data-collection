import scrapy

class ParserJobItem(scrapy.Item):
    _id = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()
    salary = scrapy.Field()
    salary_max = scrapy.Field()
    salary_min = scrapy.Field()
    salary_currency = scrapy.Field()
