from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from . models import Product
# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = 'Products/home.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'Products/detail.html'
    context_object_name = 'product'

