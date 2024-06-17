from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Quote, Company, Project

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['customer_name', 'product_name', 'quantity', 'unit_price', 'project']

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date', 'budget', 'tasks']

class ProjectDetailForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date', 'budget', 'tasks']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }