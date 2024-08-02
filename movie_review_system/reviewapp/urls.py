from django.urls import path
from .views import create, show_details, update_details, delete_details

urlpatterns = [
    path('create/', create, name='create'),
    path('details/', show_details, name='show'),
    path('update/<int:pk>/', update_details, name='update'),
    path('delete/<int:pk>/', delete_details, name='delete'),
]

