from django.urls import path
from .views import *

urlpatterns = [
    path('comment/<int:pk>/', CommentView.as_view()),
]
