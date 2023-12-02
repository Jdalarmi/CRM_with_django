from django.urls import path
from .views import CustomerListView, CustomerCreateView

app_name = "customers"
urlpatterns = [
    path('list/', CustomerListView.as_view(), name='customer-list' ),
    path('customer_create', CustomerCreateView.as_view(), name='customer-create')
]
