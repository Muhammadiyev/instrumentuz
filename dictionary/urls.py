from django.urls import path
from django.conf.urls import include,url
from rest_framework import routers
from .views import CategoryViewSet

router = routers.DefaultRouter()

router.register(r'^category',CategoryViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    # path('<int:pk>/', CategoryView.as_view()),
]
