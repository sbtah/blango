from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blog.urls", namespace="blog")),
    path("api/v1/", include("blog.api_urls")),
]
