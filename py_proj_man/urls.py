"""PyProjMan URL Handler"""
from django.conf.urls import url

from . import views

app_name = 'py_proj_man'
urlpatterns = [
    url(r'^$', views.default, name='index'),
    url(r'(?P<ws_pk>[0-9]+)/(?P<proj_pk>[0-9]+)/(?P<task_pk>[0-9]+)/$', views.task_detail, name='task'),
    url(r'(?P<ws_pk>[0-9]+)/(?P<proj_pk>[0-9]+)/$', views.project_detail, name='project'),
    url(r'(?P<pk>[0-9]+)/$', views.workspace_detail, name='workspace'),
]
