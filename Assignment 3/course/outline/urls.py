from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.searchByTitle, name="searchByTitle"),
    path("random", views.random, name="randomPage"),
    path("createpage", views.createNewPage, name="createNewPage"),
    path("editpage", views.editPage, name="editPage"),
    path("<str:TITLE>", views.getByTitle, name="getByTitle"),
]
