from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/(?P<slug>[0-9a-zA-Z/-]+)/$', views.view_category, name='view_category'),
    url(r'^(?P<slug>[0-9a-zA-Z/-]+)/$', views.view_post, name='view_post'),
]
