import os

REDIS_PASSWORD=os.getenv('REDIS_PASSWORD')
broker_url = f'redis://:{REDIS_PASSWORD}@192.168.234.128:6379/15'