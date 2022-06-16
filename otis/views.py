from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html", {})


def servicii(request):
    return render(request, "servicii.html", {})


def costuri(request):
    return render(request, "costuri.html", {})


def contact(request):
    return render(request, "contact.html", {})
