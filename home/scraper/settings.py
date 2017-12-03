import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mill_geek2.settings")

BOT_NAME = 'home'

SPIDER_MODULES = ['dynamic_scraper.spiders', 'home.scraper',]
USER_AGENT = '%s/%s' % (BOT_NAME, '1.0')

ITEM_PIPELINES = {
	'dynamic_scraper.pipelines.ValidationPipeline':400,
	'home.scraper.pipelines.DjangoWriterPipeline':800,
}

ITEM_PIPELINES = [
	'dynamic_scraper.pipelines.ValidationPipeline',
	'home.scraper.pipelines.DjangoWriterPipeline',
	]