from django.urls import path
from .views import CustomerListView

app_name = "customers"
urlpatterns = [
    path('list/', CustomerListView.as_view(), name='customer-list' )
]
