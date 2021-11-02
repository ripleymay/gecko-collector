from django.shortcuts import render
from .models import Gecko

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def geckos_index(request):
  geckos = Gecko.objects.all()
  return render(request, 'geckos/index.html', { 'geckos': geckos })