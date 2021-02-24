BOT_NAME = 'nbb'

SPIDER_MODULES = ['nbb.spiders']
NEWSPIDER_MODULE = 'nbb.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
# LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0
USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36"

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'nbb.pipelines.NbbPipeline': 300,

}