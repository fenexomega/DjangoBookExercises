from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangobook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'example_app.views.index.page',name='index'),
    url(r'^project-detail-(?P<pk>\d+)$','example_app.views.project_detail.page',name='project_detail'),
    url(r'^create_developer$','example_app.views.create_developer.page',name='create_developer'),
    url(r'^create_supervisor$','example_app.views.create_supervisor.page',name='create_supervisor'),
    url(r'^create_project$','example_app.views.create_project.page',name='create_project')
    #url(r'^connection$', 'example_app.views.connection.page', name="public_connection")
)
