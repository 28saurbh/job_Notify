
from . import views
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index),
    path('blog/<str:slug>', views.blog_page, name="blog_page")
]

urlpatterns += staticfiles_urlpatterns()