from django.shortcuts import render
from django.http import HttpResponse
from cars.models import Car
from cars.forms import CarForm

def cars_view(request):
    cars = Car.objects.all()
    return render (    
    request,
    'cars.html',
    {'cars': cars}
    )

def new_car_view(request):
    new_car_form = CarForm()
    if request.method == 'POST':
        new_car_form = CarForm(request.POST, request.FILES)
        print(new_car_form.data)
    else:
        return render(request, 'new_car.html', {'new_car_form':new_car_form})