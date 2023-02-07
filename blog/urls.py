from django.contrib import admin
from django.urls import path, include
from blog.views import *
urlpatterns = [
    path('', post_list.as_view(), name='post_list'),
    path('tags/<str:tag>/',post_list.as_view(),name='tag_post_list'),
    path('createpost/',createPostView.as_view(), name='create_post'),    
    path('like/<slug:slug>/',like_post, name='like_post'),
    path('like2/<slug:slug>/',like_post2, name='like_post2'),
    path('edit/<slug:slug>/',editPostView.as_view(), name='edit_post'),
	path('delete/<slug:slug>/',deletePostView.as_view(), name='delete_post'),
    path('<slug:slug>/', post_detail.as_view(), name='post_detail'),
    
]