from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("outl/<str:topics>", views.outline, name="outline"),
    path("search/", views.search, name="search"),
    path("new", views.new, name="new"),
    path("random", views.random_topics, name="random_topics"),
    path("edit/<str:topics>", views.edit, name="edit"),
]

handler404 = "outline.views.handler404"
