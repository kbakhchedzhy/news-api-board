"""news_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from home.views import NewsViewSet, CommentsViewSet, VoteForNews

router = routers.DefaultRouter()
router.register(r"news", NewsViewSet, basename="news_page_api")
router.register(r"comments", CommentsViewSet, basename="comments_page_api")


urlpatterns = [
    path("drf/", include(router.urls)),
    path("admin/", admin.site.urls),
    path("vote/<pk>/", VoteForNews.as_view(), name="example"),
]
