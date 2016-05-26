from django.conf.urls import url
from . import views


app_name = 'bananasorter'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^profile/$', views.profile, name='profile'),
]
