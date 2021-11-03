from django.db import models
from django.urls import reverse

# Create your models here.

class Gecko(models.Model):
    name = models.CharField(default="No Name", max_length=50)
    species = models.CharField(default="Unknown", max_length=50)
    age = models.IntegerField(default=1)
    description = models.TextField(default="None", max_length=100)

    def __str__(self):
        return (f'{self.name} is a {self.age} year old {self.species} gecko') 

    def get_absolute_url(self):
        return reverse('detail', kwargs={'gecko_id': self.id})