from django.urls import path
from webapp.views import EmployeeCreateView,EmployeeListView,EmployeeUpdateView,EmployeeDeleteView

urlpatterns = [
    path('', EmployeeListView.as_view(),name='list'),
    path('create', EmployeeCreateView.as_view(),name='create'),
    path('update/<int:pk>/',EmployeeUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',EmployeeDeleteView.as_view(),name='delete')

]