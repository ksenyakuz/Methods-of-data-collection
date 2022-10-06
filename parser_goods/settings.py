# Scrapy settings for parser_goods project

BOT_NAME = 'parser_goods'

SPIDER_MODULES = ['parser_goods.spiders']
NEWSPIDER_MODULE = 'parser_goods.spiders'

LOG_ENABLED = True
LOG_LEVEL = "DEBUG"

IMAGES_STORE = 'photos'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 8

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'parser_goods.pipelines.ParserGoodsPipeline': 400,
   'parser_goods.pipelines.PhotosPipeline': 200
}
