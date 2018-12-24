from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'blog'
"""
urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/', views.results, name='results'),
    path('new/', views.new_post, name='new_post'),
    path('edit/', views.edit_post, name='edit_post'),
]
"""
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^post/new/$', views.new_post, name='new_post'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.edit_post, name='edit_post'),
]
