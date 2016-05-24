from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'banana.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('bananasorter.urls')),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
