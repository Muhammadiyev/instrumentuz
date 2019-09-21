from rest_framework import serializers
from .models import Comment
from instruments.serializers import InstrumentAllSerializer

class CommentSerializer(serializers.ModelSerializer):
    
    category = InstrumentAllSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
