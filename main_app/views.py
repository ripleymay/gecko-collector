from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Gecko, Snack, TankItem
from .forms import SnackForm

class GeckoCreate(CreateView):
  model = Gecko
  fields = ['name', 'species', 'age', 'description']

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
  not_in_geckos_tank = TankItem.objects.exclude(id__in=gecko.tank_items.all().values_list('id'))
  snack_form = SnackForm()
  return render(request, 'geckos/detail.html', { 
    'gecko': gecko, 'snack_form': snack_form, 'tank_items': not_in_geckos_tank
  })

def add_snack(request, gecko_id):
  form = SnackForm(request.POST)
  if form.is_valid():
    new_snack = form.save(commit=False)
    new_snack.gecko_id = gecko_id
    new_snack.save()
  return redirect('detail', gecko_id=gecko_id)

class TankItemList(ListView):
  model = TankItem

class TankItemDetail(DetailView):
  model = TankItem

class TankItemCreate(CreateView):
  model = TankItem
  fields = '__all__'

class TankItemUpdate(UpdateView):
  model = TankItem
  fields = ['name', 'heated']

class TankItemDelete(DeleteView):
  model = TankItem
  success_url = '/tankitems/'

def assoc_tankitem(request, gecko_id, tankitem_id):
  Gecko.objects.get(id=gecko_id).tank_items.add(tankitem_id)
  return redirect('detail', gecko_id=gecko_id)

def unassoc_tankitem(request, gecko_id, tankitem_id):
  Gecko.objects.get(id=gecko_id).tank_items.remove(tankitem_id)
  return redirect('detail', gecko_id=gecko_id)