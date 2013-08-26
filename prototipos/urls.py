# encoding: utf-8

from django.conf.urls.defaults import patterns, include

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings

from views import IndexView

admin.autodiscover()

urlpatterns = patterns('',
                      (r'^admin/', include(admin.site.urls)),
                      (r'^index.html$', IndexView.as_view()),
                      (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))
