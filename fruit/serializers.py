from rest_framework import serializers
from .models import Fruit,Review



class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields = '__all__'