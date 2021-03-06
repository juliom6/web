from django.conf.urls import patterns, include, url
from django.conf import settings
from search.views import buscador, resultados, audioyvideo, audio
from search.views import video, celulares, producto

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'search.views.buscador'),
    # url(r'^web/', include('web.foo.urls')),

    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
	url(r'^resultados/$', 'search.views.resultados'),
	url(r'^audioyvideo/$', 'search.views.audioyvideo'),
	url(r'^audio/$', 'search.views.audio'),
	url(r'^video/$', 'search.views.video'),
	url(r'^celulares/$', 'search.views.celulares'),
	url(r'^computacion/$', 'search.views.computacion'),
	url(r'^libros/$', 'search.views.libros'),
	url(r'^instrumentosmusicales/$', 'search.views.instrumentosmusicales'),
	url(r'^producto/(\d+)/', 'search.views.producto'),
)
