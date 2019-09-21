from django.shortcuts import render
from rest_framework import generics
from .serializers import CommentSerializer


class CommentView(generics.CreateAPIView):
    serializer_class = CommentSerializer