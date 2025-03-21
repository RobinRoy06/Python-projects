from django.forms import ModelForm, forms
from .models import *
import datetime
class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ["title","description","genre","post_creation","rating"]
       

class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ["username","password"]