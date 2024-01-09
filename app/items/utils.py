from .models import Item
from django.db import models

def calculate_total_value():
    total_value =  Item.objects.all().aggregate(models.Sum('value'))['value__sum'] or 0.00
    return round(total_value, 2)
