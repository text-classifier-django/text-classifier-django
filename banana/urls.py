from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('bananasorter.urls')),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^login/$','django.contrib.auth.views.login', {'template_name': 'login.html'}),
	url(r'^logout/$','django.contrib.auth.views.logout', {'next_page': '/login/'}),
    url(r'^admin/', include(admin.site.urls)),
]
