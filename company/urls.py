from django.urls import path
from .views import *

urlpatterns = [
    path('', FirmListView.as_view()),
    path('<int:pk>/', FirmsAllView.as_view()),
]