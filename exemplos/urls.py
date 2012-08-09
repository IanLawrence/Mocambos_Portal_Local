from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout
from django.conf import settings
# For Django-Filer
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

## For Django-Filebrowser >= 3.4.0
#from filebrowser.sites import site

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Mocambos_Portal.views.home', name='home'),
    # url(r'^Mocambos_Portal/', include('Mocambos_Portal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', {'template_name' : 'registration/password_reset.html',  'post_reset_redirect': '/logout/' }),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'baobaxia.views.index', name='index'),
    url(r'^publica', 'baobaxia.views.publica', name='index'),
    url(r'^accounts/', include('registration.backends.default.urls')),
#    (r'^accounts/login/$',  login, include('registration.backends.default.urls')),
#    (r'^accounts/logout/$', logout, include('registration.backends.default.urls')),
    
#    # For Django-Grappelli
#    url(r'^grappelli/', include('grappelli.urls')),
    ## For Django-Filebrowser 3.4.0
#    url(r'^admin/filebrowser/', include(site.urls)),
#    # For Django-Filebrowser 3.3.0
#    url(r'^admin/filebrowser/', include('filebrowser.urls')),
    # For django_bfm
#    url(r'^files/', include('django_bfm.urls')),
)

# For Django-Filer
#urlpatterns += staticfiles_urlpatterns()

# Let Django serve media files in Debug Mode
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
