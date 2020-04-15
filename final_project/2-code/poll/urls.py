from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views as views
app_name = 'poll'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex : /poll/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    #url(r'^detail/', views.detail, name='detail'),
    # ex : /poll/5/results/
    url(r'^(?P<question_id>[0-9]+)/results', views.results, name='results'),
    # ex : /poll/5/vote
    #path('blog/page<int:num>/', views.vote),
    url(r'^(?P<question_id>[0-9]+)/vote', views.vote, name='vote'),

]
#   url(r'^register/', views.user_register, name='register'),
