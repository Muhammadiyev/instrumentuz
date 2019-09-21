from rest_framework import serializers
from .models import Category, Property, Guarantee_Period

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'



class PropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = Property
        fields = '__all__'


class Guarantee_PeriodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Guarantee_Period
        fields = '__all__'

