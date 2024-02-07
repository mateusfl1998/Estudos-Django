from django.shortcuts import render, redirect
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
    if request.method == 'POST':
        new_car_form = CarForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('car_list')
        print(new_car_form.data)
    else:
        new_car_form = CarForm()
        return render(request, 'new_car.html', {'new_car_form':new_car_form})