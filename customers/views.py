from typing import Any
from django.db import models
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Customer
from .forms import CustomerForm
from django.urls import reverse


class CustomerListView(ListView):
    template_name = "customers/customer_list.html"
    model = Customer
    queryset = Customer.objects.all()

class CustomerCreateView(CreateView):
    template_name = "customers/customer.html"
    form_class = CustomerForm

    def form_valid(self, form):
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('customers:customer-list')
    
class CustomerUpdateView(UpdateView):
    template_name = "customers/customer.html"
    form_class = CustomerForm

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Customer, id=id)

    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("customers:customer-list")
    
    
class CustomerDeleteView(DeleteView):
    pass