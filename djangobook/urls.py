from django.conf.urls import patterns, include, url
from django.views.generic import CreateView, DetailView, UpdateView
from example_app.models import Project,Task, Developer
from django.views.generic.list import ListView
from django.contrib import admin
from django.contrib.auth.decorators import login_required

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
    url(r'^create_project$',login_required(CreateView.as_view(model=Project, 
        template_name="create_project.html",success_url='index')),name="create_project"),
    url(r'^create_task$',login_required(CreateView.as_view(model=Task, 
        template_name="create_task.html",success_url="index")),name="create_task"),
    url(r'^connection$', 'example_app.views.connection.page', name="public_connection"),
    url(r'^project_list$',login_required(ListView.as_view(model=Project,
        template_name="detail_project.html")),name="project_detail"),
    url(r'^detail_task_(?P<pk>\d+)$','example_app.views.detail_task.page',name="detail_task"),
    url(r'^task_list$',"example_app.views.list_task.page",name="list_task"),
    url(r'^update_task_(?P<pk>\d+)$',UpdateView.as_view(model=Task,template_name="update_task.html",success_url="index"),name="update_task"),
    url(r'^list_developers$',ListView.as_view(model=Developer,template_name='list_developer.html'),name='list_developer'),
    url(r'^logout$',"example_app.views.logout.page",name="logout")
)
