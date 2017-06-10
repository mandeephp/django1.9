
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.posts_list, name = "posts_list"),
    url(r'^create', views.posts_create, name = ""),
    url(r'^(?P<id>\d+)/$', views.posts_detail, name = "post_detail"),
    #url(r'^detail/', views.posts_detail, name = ""),
    url(r'^(?P<id>\d+)/edit/$', views.posts_update, name = 'edit'),
    url(r'^(?P<id>\d+)/delete', views.posts_delete, name = ""),
    url(r'^user', views.posts_user, name = ""),
]
