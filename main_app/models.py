from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.

SNACKS = (
    ('B', 'Beetles'),
    ('C', 'Crickets'),
    ('M', 'Mealworms'),
    ('S', 'Shed skin'),
    ('W', 'Waxworms')
)

class TankItem(models.Model):
  name = models.CharField(max_length=50)
  heated = models.BooleanField(default=False)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('tankitems_detail', kwargs={'pk': self.id})

class Gecko(models.Model):
    name = models.CharField(default="No Name", max_length=50)
    species = models.CharField(default="Unknown", max_length=50)
    age = models.IntegerField(default=1)
    description = models.TextField(default="None", max_length=100)
    tank_items = models.ManyToManyField(TankItem)

    def __str__(self):
        return (f'{self.name} is a {self.age} year old {self.species} gecko') 

    def get_absolute_url(self):
        return reverse('detail', kwargs={'gecko_id': self.id})

    def is_full(self):
        return True if self.snack_set.filter(date=date.today()).count() >= 1 else False

class Snack(models.Model):
    food = models.CharField(
        max_length=1,
        choices=SNACKS,
        default=SNACKS[1][0])
    date = models.DateField('Date fed')
    gecko = models.ForeignKey(Gecko, on_delete=models.CASCADE)

    def __str__(self):
        return (f'{self.get_food_display()} on {self.date}')

    class Meta:
        ordering = ['-date']