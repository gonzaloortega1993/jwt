from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views

from django.conf.urls import url

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    url(r'^auth/', include('djoser.urls')),
    #path('auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.authtoken')),

    url(r'^auth/', include('djoser.urls.jwt')),
]