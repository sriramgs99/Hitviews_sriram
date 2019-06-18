"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from posts import views
app_name = 'posts'
urlpatterns = [
    # path('', views.post_list, name='post_list'),
    url(r'^$', views.post_list, name="post_list"),
    # url(r'like_post/$', views.like_post, name="like_post"),
    url(r'^like_post/(?P<id>\d+)/$',views.like_post, name="like_post"),


    #url('home', views.post_list, name="post_list"),
    url(r'^posts/(?P<id>\d+)/$',views.post_detail, name="post_detail"),
        # url(r'^posts/(?P<id>\d+)/(?P<slug>[\w-]+)/$',views.post_detail, name="post_detail"),

    url(r'post_create/$', views.post_create, name="post_create"),

]
