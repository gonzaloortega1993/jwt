from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from snippets import views


# Creo router y registro las viewsets.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet,base_name="users")


# Algunas URLs son determinadas automaticamente por el router.
urlpatterns = [
    path('', views.api_root),
    path('', include(router.urls)),
]