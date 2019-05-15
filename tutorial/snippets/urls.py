from django.conf.urls import include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from rest_framework.routers import DefaultRouter
from rest_framework import renderers

# Create a sourter and register our viewsets with it
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# Bound resources into concrete views and now register the views as usual
urlpatterns = [
    path('',include(router.urls))
]
