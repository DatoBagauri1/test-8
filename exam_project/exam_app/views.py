from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')

def films(request):
    fav_films = ['Lord Of the Rings', 'Fast And Furious', 'Need For Speed']
    rates = [9.0, 6.8, 6.4]
    films_data = zip(fav_films, rates)
    return render(request, 'films.html', {'films_data': films_data})

