from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

class CarView(View):
    
    def get(self,request):
        cars = Car.objects.all()
        return render (    
        request,
        'cars.html',
        {'cars': cars}
        )
    
class CarListView(ListView):
    model =  Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
        return cars 
        
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url =   '/cars_list/'

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'
    success_url = '/cars/'

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'