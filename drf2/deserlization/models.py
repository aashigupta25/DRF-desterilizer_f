from django.db import models

# Create your models here.
class Business(models.Model):
    product: models.CharField(max_length=100)
    quality_percentage: models.IntegerField()
    demand_percent: models.IntegerField()
    earning: models.IntegerField()
    expanses: models.IntegerField()
    unique_products: models.CharField(max_length=100)

