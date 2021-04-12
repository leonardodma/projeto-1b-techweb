from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tags/<str:tag_>/', views.tags, name='tags'),
    path('/tags', views.tags2, name='tags2'),
    path('/tagslist', views.tags_list, name='tags_list'),
]