from webapp.models import Employee
from django import forms

class EmployeeModelForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    class Meta:
        model = Employee
        fields = ('name','email','gender','date_of_birth','send_update','photo')


