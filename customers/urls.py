from django.urls import path
from .views import CustomerListView, CustomerCreateView, CustomerUpdateView

app_name = "customers"
urlpatterns = [
    path('list/', CustomerListView.as_view(), name='customer-list' ),
    path('customer_create', CustomerCreateView.as_view(), name='customer-create'),
    path('<int:id>/', CustomerUpdateView.as_view(), name='customer-update'),
]
