from django.shortcuts import render

from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, "gestion/home.html")

def adminInicio(request):
    return render(request, "gestion/index.html")
