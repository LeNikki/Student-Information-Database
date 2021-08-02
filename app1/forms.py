#from django.forms import ModelForm
from django import forms
from .models import App1Students

class StudentsForm(forms.ModelForm):
    class Meta:
        model = App1Students    # make form for this model
        fields = "__all__"      #using all fields

#import form in views.py