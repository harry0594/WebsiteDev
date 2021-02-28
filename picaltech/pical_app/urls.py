from django.urls import path
from pical_app import views


app_name ='pical_app'

urlpatterns = [
    path('blog/',views.blog,name='blog'),
    path('blog_single/',views.blog_single,name="blog_single"),
    path('inner_page/',views.inner_page,name='inner_page'),
    path('ourworks/',views.ourworks,name='ourworks'),
]
