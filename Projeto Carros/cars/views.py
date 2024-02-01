from django.shortcuts import render
from django.http import HttpResponse

def cars_view(request):
    return HttpResponse('''<h1>Meus Carros</h1>
                        Só carro top na Mtec Carros!    
                        ''')
