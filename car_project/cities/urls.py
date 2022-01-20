from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='city_index'),
    path('create/', views.create_city, name='city_create'),
    path('edit/<int:city_id>/', views.edit, name='city_edit'),
    path('<int:city_id>/city_car_create/', views.city_car_create, name='city_car_create'),
    path('city_car_list/', views.city_car_index, name='city_car_index'),
    path('delete/<int:city_id>/', views.delete, name='city_delete'),
    path('<int:city_id>/download_file/', views.download_city_file, name='city_file_download'),

]
