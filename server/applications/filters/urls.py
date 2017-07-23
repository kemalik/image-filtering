from django.conf.urls import url, include
from rest_framework import routers
from .api.viewsets import ResourceViewSet

router = routers.DefaultRouter()
router.register(r'', ResourceViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]