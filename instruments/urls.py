from django.urls import path
from django.conf.urls import include,url
from rest_framework import routers
from .views import (
    InstrumentViewSet,
    InstrumentAllView,
    InstrumentDiscountViewSet,
    SearchViewSet,
)

router = routers.DefaultRouter()

router.register(r'^instruments',InstrumentViewSet)
router.register(r'^discount',InstrumentDiscountViewSet)
router.register(r'^description',InstrumentDiscountViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    path('search/', SearchViewSet.as_view()),
    path('instrument/<int:pk>/', InstrumentAllView.as_view()),
]

