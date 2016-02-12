from django.conf.urls import include, url
from django.contrib import admin
from regis import views

urlpatterns = [
    # Examples:
    url(r'^$', 'regis.views.home', name='home'),
    url(r'^(?P<zeal_id>[0-9]+)/display/$', views.display, name='display'),
    url(r'^admin/', include(admin.site.urls)),
]
