from turtle import textinput
from django.forms import *
from .models import *

class PromptForm (ModelForm):
    class Meta:
        widgets = {
            'prompt':Textarea()
        }
