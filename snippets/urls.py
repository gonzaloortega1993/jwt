from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from snippets import views


# Creo router y registro las viewsets.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet,base_name="users")


# Algunas URLs son determinadas automaticamente por el router.
urlpatterns = [
    path('', views.api_root),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('djoser.urls')),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^auth/', include('djoser.urls.authtoken')),
    url(r'^auth/', include('djoser.urls.jwt')),
]
