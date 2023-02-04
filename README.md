# CRUD_Operation_in_Django

![img1](https://images.ladepeche.fr/api/v1/images/view/62703bb3f6394c635b418365/large/image.jpg?v=2)


settings.py:
````python

````
models.py:
````python

````

views.py:
````python
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
````
mysite/urls.py:
````python
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from mysite import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('webapp.urls')),
]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
````
webapp/urls.py:
````python
from django.urls import path
from webapp.views import EmployeeCreateView,EmployeeListView,EmployeeUpdateView,EmployeeDeleteView

urlpatterns = [
    path('', EmployeeListView.as_view(),name='list'),
    path('create', EmployeeCreateView.as_view(),name='create'),
    path('update/<int:pk>/',EmployeeUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',EmployeeDeleteView.as_view(),name='delete')

]
````
home.html
````html
{%extends "index.html"%}
{% load crispy_forms_tags %}
{%block content%}

<div class="container mx-auto p-2 mt-2">
    <ul class="list-inline">
        <li class="list-inline-item">
            <a href="{%url 'create'%}" class="btn btn-primary"><i class="fa-sharp fa-solid fa-plus"></i>&nbsp;Add Employee</a>
        </li>
    </ul>

    <table class="table table-sm table-success table-striped-columns">
        <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">Firstname</th>
              <th scope="col">Name</th>
              <th scope="col">Email</th>
              <th scope="col">Gender</th>
              <th scope="col">DOB</th>
              <th scope="col">Send Update</th>
              <th scope="col">Photo</th>
              <th scope="col">Update</th>
              <th scope="col">Delete</th>

            </tr>
        </thead>
        <tbody class="table-group-divider">
            {%for employee in employee_list%}
            <tr>
              <th scope="row">{{forloop.counter}}.</th>
              <td><img src="{{employee.photo.url}}" class="rounded-circle" width="50px" height="50px">&nbsp;&nbsp;{{employee.firstname}}</td>
              <td>{{employee.name}}</td>
              <td>{{employee.email}}</td>
              <td>{{employee.get_gender_display}}</td>
              <td>{{employee.date_of_birth}}</td>
              <td>{{employee.send_update}}</td>
              <td>Photo</td>
              <td><a href="{%url 'update' pk=employee.pk%}"><i class="fa-solid fa-user-pen fa-2x"></i></a></td>
              <td><a href="#employeeModel{{employee.pk}}" data-bs-target="#employeeModel{{employee.pk}}" data-bs-toggle="modal"><i class="fa-solid fa-user-minus text-danger fa-2x"></i></a></td>
            </tr>

            <div class="modal fade" id="employeeModel{{employee.pk}}" aria-hidden="true" aria-labelledby="employeeModalToggleLabel" tabindex="-1">
                <div class="modal-dialog">
                  <div class="modal-content">
                    <div class="modal-header">
                      <div>
                        <h1 class="modal-title fs-5" id="exampleModalToggleLabel">Are you sure, you want to delete {{employee.name}}'s detail ?</h1>
                        <ul class="list-inline text-end">
                            <li class="list-inline-item">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                            </li>
                            <li class="list-inline-item">
                                <a href="{%url 'delete' pk=employee.pk%}" class="btn btn-danger">Delete</a>
                            </li>
                          </ul>
                      </div>

                    </div>
                  </div>
                </div>
              </div>

            {%endfor%}
        </tbody>
    </table>
</div>

{%endblock%}
````

![img1](./images/doc1.png)