from django.shortcuts import render
from rest_framework import generics,viewsets
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import CategorySerializer
from .models import Category, Property

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

