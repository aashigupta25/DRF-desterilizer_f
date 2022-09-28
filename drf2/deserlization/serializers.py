from rest_framework import serializers
from .models import Business

class Businessserilizer(serializers.Serializer):
    product: serializers.CharField(max_length=100)
    quality_percentage: serializers.IntegerField()
    demand_percent: serializers.IntegerField()
    earning: serializers.IntegerField()
    expanses: serializers.IntegerField()
    unique_products: serializers.CharField(max_length=100)

