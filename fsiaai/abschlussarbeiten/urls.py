from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all', views.allentries, name='all'),
    path('<int:thesis_id>/', views.detail, name='detail'),
]
