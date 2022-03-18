import os
import django
from django.utils import timezone
os.environ.setdefault("DJANGO_SETTINGS_MODULE","V01.settings")
django.setup()

from redis_cache.models import Products

for i in range (1000) :
    Products.objects.create(name="Afred",description="Ger",price)