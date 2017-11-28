from __future import unicode_literals
from dynamic_scraper.spiders.django_checker import DjangoChecker
from home.models import Article

class ArticleChecker(DjangoChecker):

	name = 'article_checker'

	def __init__(self, *args, **kwargs):
		self.set_ref_object(Article, **kwargs)
		self.scraper = self.ref_object.wizard_website.scraper
		#self.scrape_url = self.ref_object.url
		self.scheduler_runtime = self.ref_object.checker_runtime
		super(ArticleChecker, self).__init__(self, *args, **kwargs)