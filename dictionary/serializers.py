from rest_framework import serializers
from .models import (
    Category, Property,
    Guarantee_Period,
    Property_unit,Period_term
)

class Period_termSerializer(serializers.ModelSerializer):

    class Meta:
        model = Period_term
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class PropertyUnitSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Property_unit
        fields = '__all__'

class PropertySerializer(serializers.ModelSerializer):

    property_unit = PropertyUnitSerializer(read_only=True)
    class Meta:
        model = Property
        fields = '__all__'


class Guarantee_PeriodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Guarantee_Period
        fields = '__all__'

