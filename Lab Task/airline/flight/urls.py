from django.urls import path
from .import views
urlpatterns = [
    path('', views.tooba, name='index'),
    path('list/', views.list, name='list'),
]
