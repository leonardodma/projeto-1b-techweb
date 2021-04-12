from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/tags', views.tags, name='tags'),
    path('/tags_list', views.tags_list, name='tags_list'),
]