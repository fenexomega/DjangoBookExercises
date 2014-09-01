from django.conf.urls import patterns, include, url
from django.views.generic import CreateView
from example_app.models import Project,Task
from django.views.generic.list import ListView


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
    # url(r'^create_project$','example_app.views.create_project.page',name='create_project'),
    url(r'^create_project$',CreateView.as_view(model=Project, template_name="example_app/create_project.html",success_url='index'),name="create_project"),
    url(r'^create_task$',CreateView.as_view(model=Task, template_name="example_app/create_task.html",success_url="index"),name="create_task"),
    #url(r'^connection$', 'example_app.views.connection.page', name="public_connection")
    url(r'^project_list$',ListView.as_view(model=Project,template_name="example_app/project_detail.html"),name="project_detail")
)
