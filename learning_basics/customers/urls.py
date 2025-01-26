from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.customers),
    path('customers/customer_details/<int:id>', views.customer_details),
]