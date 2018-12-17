from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.detail, name='detail'),
    path('<int:post_id>/', views.results, name='results'),
    path('new/', views.new_post, name='new post'),
]