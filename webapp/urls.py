from django.urls import path
from . import views

urlpatterns = [
    path('create_data/', views.create_data),
    path('read/', views.read_data),
    path('update/<int:Stu_id>/', views.update_data),
    path('delete/<int:Stu_id>/', views.delete_data),
]
