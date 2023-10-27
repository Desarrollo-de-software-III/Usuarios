from .views import *
from rest_framework import routers
from django.urls import path, include
router = routers.DefaultRouter()

# define the router path and viewset to be used
router.register(r'user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
