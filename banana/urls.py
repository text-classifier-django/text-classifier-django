from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('bananasorter.urls')),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
