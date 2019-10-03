from rest_framework import serializers
from .models import Instrument, Image, Instrument_in_Discount,Description
from dictionary.serializers import (
    Guarantee_PeriodSerializer,
    PropertySerializer,
    Period_termSerializer,
)

class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'


class InstrumentSerializer(serializers.ModelSerializer):
    
    image = ImageSerializer(many=True,read_only=True)

    class Meta:
        model = Instrument
        fields = ('id','image','name', 'price','reate','date')


class InstrumentAllSerializer(serializers.ModelSerializer):
    
    image = ImageSerializer(many=True,read_only=True)
    guarantee_period = Guarantee_PeriodSerializer(read_only=True)
    property = PropertySerializer(read_only=True)

    class Meta:
        model = Instrument
        fields = '__all__'

class InstrumentDiscountSerializer(serializers.ModelSerializer):
    
    discount_term = Period_termSerializer(read_only=True)
    instrument = InstrumentAllSerializer(read_only=True)
   
    class Meta:
        model = Instrument_in_Discount
        fields = '__all__'


class InstrumentDescriptionSerializer(serializers.ModelSerializer):
    
    #discount_term = ImageSerializer(many=True,read_only=True)
    #instrument = InstrumentAllSerializer(read_only=True)
   
    class Meta:
        model = Description
        fields = ('id','name', 'title', 'description')