from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from baseapp import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'devopt.views.home', name='home'),
    # url(r'^devopt/', include('devopt.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index),
    url(r'^catal/$', views.testcataloh),
    url(r'^registration/$', 'accounts.views.registr' ),
    url(r'^catalog/$', views.catalogfull),
    url(r'^catalog/detail/(\d+)/$', views.product_detail),
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
    url(r'^accounts/profile/$', views.profile_test ),
    url(r'^add_cart/$', views.add_to_cart),



)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
    )