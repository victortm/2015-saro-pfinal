from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'pfinal.views.index'),
	url(r'^ayuda$', 'pfinal.views.help'),
	url(r'^todas$', 'pfinal.views.all'),
	url(r'^login$', 'pfinal.views.auth'),
    url(r'^logout$', 'django.contrib.auth.views.logout',
		{'next_page': '/'}),
    url(r'^actualizar$', 'pfinal.views.update'),
	url(r'^actividad/(.*)$', 'pfinal.views.event'),
	url(r'^rss$', 'pfinal.views.indexrss'),
	url(r'^(.*)/rss$', 'pfinal.views.rss'),
    url(r'^(.*)$', 'pfinal.views.user'),    
)
