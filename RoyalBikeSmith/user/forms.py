from django import forms
from .models import Customer, JobCard

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ('user',)

class JobCardForm(forms.ModelForm):
    class Meta:
        model = JobCard
        exclude = ('customer',)