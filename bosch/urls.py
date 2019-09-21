from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/company/', include('company.urls')),
    path('api/v1/', include('instruments.urls')),
    path('api/v1/', include('dictionary.urls')),
    path('api/v1/news/', include('comments.urls')),
]
