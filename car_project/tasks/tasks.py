import os
import csv
from celery import Celery


celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")


@celery.task(name="create_task")
def download_file(filepath):
	"""
	
	:param filepath: path of file
	:return: celery task
	"""
	if filepath:
		with open("%s" % filepath, "w+") as f:
			if type == 'csv':  # Logics for preparing the file
				pass
	
	return filepath


