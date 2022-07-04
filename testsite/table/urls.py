from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('routes/', views.getroutes, name='testhome'),
    path('table/', views.gettable, name='Table'),
    path('table/<str:pk>/update', views.updateTable, name='Update-table'),
    path('table/<str:pk>/', views.gettableone, name='Tableid'),
]