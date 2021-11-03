from django.forms import ModelForm
from .models import Snack

class SnackForm(ModelForm):
  class Meta:
    model = Snack
    fields = ['date', 'food']