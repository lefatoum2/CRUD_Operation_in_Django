from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from webapp.models import Employee
from webapp.forms import EmployeeModelForm

# Create your views here.
class EmployeeListView(ListView):
    model = Employee
    template_name = 'home.html'
    context_object_name = 'employee_list'
    success_url = '/'



class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeModelForm
    template_name = 'employee_form.html'
    success_url = '/'


class EmployeeUpdateView(UpdateView):
    model=Employee
    form_class = EmployeeModelForm
    template_name = 'employee_form.html'
    success_url = '/'


class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = '/'

    def get(self,request, *args, **kwargs):
        return self.delete(request,*args, **kwargs)