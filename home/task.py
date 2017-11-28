from celery.task import task

from dynamic_scraper.utils.task_utils import TaskUtils
from home.models import WizardWebsite, Article

@task()
def run_spider():
	t = TaskUtils()
	t.run_spider(WizardWebsite, 'scraper', 'scraper_runtime', 'article_spider')

@task()
def run_checker():
	t = TaskUtils()
	t.run_checkers(Article, 'wizard_website_scraper', 'checker_runtime', 'article_checker')