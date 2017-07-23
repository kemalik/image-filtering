from django.conf.urls import url, include
from django.contrib import admin
from applications.images import urls as image_urls
from applications.filters import urls as filter_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/images/', include(image_urls, namespace='images')),
    url(r'^api/filter/', include(filter_urls, namespace='filters'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
