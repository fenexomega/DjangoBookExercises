from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangobook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #	url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'example_app.views.index.page'),
    url(r'^connection$', 'example_app.views.connection.page', name="public_connection")
)
