from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='party_index'),
    path('create/', views.create_party, name='party_create'),
    path('edit/<int:party_id>/', views.edit, name='party_edit'),
    path('delete/<int:party_id>/', views.delete, name='party_delete'),

]
