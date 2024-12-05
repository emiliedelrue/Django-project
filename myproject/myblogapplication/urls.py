from django.urls import path
from . import views 

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('post/new/', views.create_post, name='create_post'),
    path('post/<int:id>/edit/', views.edit_post, name='edit_post'),
    path('post/<int:id>/delete/', views.delete_post, name='delete_post'),
    path('post/<int:id>/comment/', views.add_comment, name='add_comment'),
    path('post/<int:id>/comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('post/<int:id>/comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]