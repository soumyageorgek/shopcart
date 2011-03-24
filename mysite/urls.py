from django.conf.urls.defaults import *
from mysite.views import hello, show_color, post_comment, login, set_color, current_datetime, register, logout, add
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    ('^hello/$', hello),
    ('^show/$', show_color),
    ('^set/$', set_color),
    ('^post/$', post_comment),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/media/SOUMYA/shopcart/mysite/static/', 'show_indexes': True}),
    ('^login/$', login),
    ('^logout/$', logout),
    ('^time/$', current_datetime),
    ('^register/$', register),
    ('^add/$', add),
)
