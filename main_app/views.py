from django.shortcuts import render

class Gecko():
  def __init__(self, name, species, age, description):
    self.name = name
    self.species = species
    self.age = age
    self.description = description

geckos = [
  Gecko('Corn Dog', 'Leopard', 8, 'Young and fiesty'),
  Gecko('Lady', 'Crested', 16, 'Very regal, lives to be held'),
  Gecko('Lil guy', 'Common House', 5, "He's little but can fend for himself!")
]

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def geckos_index(request):
    return render(request, 'geckos/index.html', { 'geckos': geckos })