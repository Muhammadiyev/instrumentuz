from django.shortcuts import render
from rest_framework import generics
from .serializers import FirmsSerializer,FirmsAllSerializer
from .models import Firm

class FirmListView(generics.ListAPIView):
    serializer_class = FirmsSerializer
    queryset = Firm.objects.all()


class FirmsAllView(generics.RetrieveAPIView):
    serializer_class = FirmsAllSerializer
    queryset = Firm.objects.all()

