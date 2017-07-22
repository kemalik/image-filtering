from django.conf.urls import url, include
from rest_framework import routers
from .api.viewsets import ImagesViewSet

router = routers.DefaultRouter()
router.register(r'', ImagesViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]