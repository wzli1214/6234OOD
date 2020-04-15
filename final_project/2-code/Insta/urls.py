
from django.urls import path, include

from Insta.views import PostListView, PostDetailView, PostCreateView, PostUpdateView

urlpatterns = [
    path('', PostListView.as_view()),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post'),
    path('post/new/', PostCreateView.as_view(), name='make_post'),
    path('post/edit/<int:pk>', PostUpdateView.as_view(), name='post_edit'),

     
]


