from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Instrument, Instrument_in_Discount, Description
from .serializers import (
    InstrumentSerializer,
    InstrumentAllSerializer,
    InstrumentDiscountSerializer,
    InstrumentDescriptionSerializer,
)



class InstrumentDiscountViewSet(viewsets.ModelViewSet):
    queryset = Instrument_in_Discount.objects.filter()
    serializer_class = InstrumentDiscountSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ['instrument__firm']



class InstrumentViewSet(viewsets.ModelViewSet):
    queryset = Instrument.objects.filter()
    serializer_class = InstrumentSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ['categories','firm']
    search_fields = ['name']

class InstrumentAllView(generics.RetrieveAPIView):
    serializer_class = InstrumentAllSerializer
    queryset = Instrument.objects.all()



class InstrumentDescriptionViewSet(viewsets.ModelViewSet):
    queryset = Description.objects.filter()
    serializer_class = InstrumentDescriptionSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ['instrument__firm','instrument__categories']


class SearchViewSet(generics.ListAPIView):
    __basic_fields = ('name','price')
    queryset = Instrument.objects.filter()
    serializer_class = InstrumentAllSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields


class NewInstrumentModelViewSet(viewsets.ModelViewSet):
    queryset = Instrument.objects.all().order_by("-date")
    serializer_class = InstrumentAllSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ['firm']
