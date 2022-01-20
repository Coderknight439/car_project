from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='car_index'),
    path('create/', views.create_car, name='car_create'),
    path('edit/<int:car_id>/', views.edit, name='car_edit'),
    path('delete/<int:car_id>/', views.delete, name='car_delete'),

]
