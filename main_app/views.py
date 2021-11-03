from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Gecko

class GeckoCreate(CreateView):
  model = Gecko
  fields = '__all__'

class GeckoUpdate(UpdateView):
  model = Gecko
  fields = ['species', 'age', 'description']

class GeckoDelete(DeleteView):
  model = Gecko
  success_url = '/geckos/'

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def geckos_index(request):
  geckos = Gecko.objects.all()
  return render(request, 'geckos/index.html', { 'geckos': geckos })

def geckos_detail(request, gecko_id):
  gecko = Gecko.objects.get(id=gecko_id)
  return render(request, 'geckos/detail.html', { 'gecko': gecko })