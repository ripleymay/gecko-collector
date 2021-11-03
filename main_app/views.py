from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Gecko
from .forms import SnackForm

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
  snack_form = SnackForm()
  return render(request, 'geckos/detail.html', { 
    'gecko': gecko, 'snack_form': snack_form 
  })

def add_snack(request, gecko_id):
  form = SnackForm(request.POST)
  if form.is_valid():
    new_snack = form.save(commit=False)
    new_snack.gecko_id = gecko_id
    new_snack.save()
  return redirect('detail', gecko_id=gecko_id)