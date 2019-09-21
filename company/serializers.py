from rest_framework import serializers
from dictionary.serializers import CategorySerializer
from .models import Firm


class FirmsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Firm
        fields = '__all__'

class FirmsAllSerializer(serializers.ModelSerializer):
    
    category = CategorySerializer(many=True,read_only=True)

    class Meta:
        model = Firm
        fields = ('id', 'name', 'image','category')