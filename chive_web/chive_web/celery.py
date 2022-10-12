import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chive_web.settings')

app = Celery('chive_web')
app.config_from_object('django.conf:settings', namespace='CELERY')

CELERY_BROKER_URL = 'redis://chive_web-redis:6379'

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'get_coins_data_20': {
        'task': 'crypto_info.tasks.get_coins_data_binance',
        'schedule': 20
    },
    'get_binance_news_120s': {
        'task': 'crypto_info.tasks.get_binance_news',
        'schedule': 120
    }
}
