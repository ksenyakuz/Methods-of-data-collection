# Scrapy settings for instaParser project

BOT_NAME = 'instaParser'

SPIDER_MODULES = ['instaParser.spiders']
NEWSPIDER_MODULE = 'instaParser.spiders'

LOG_ENABLED = True
LOG_LEVEL = 'INFO'

IMAGES_STORE = 'photos'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 10

# Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = 0.5

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Configure item pipelines
ITEM_PIPELINES = {
    'instaParser.pipelines.InstaParserPipeline': 300,
    'instaParser.pipelines.InstaUserPhotosPipeline': 100
}

# Enable and configure the AutoThrottle extension (disabled by default)
AUTOTHROTTLE_ENABLED = True

# The initial download delay
AUTOTHROTTLE_START_DELAY = 3

# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60

# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = True
