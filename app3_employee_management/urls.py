from django.urls import path
from .views import EmployeeAdd, EmployeeDelete, EmployeeEdit, EmployeeDocumentsAdd, EmployeeDocumentsDelete, EmployeeSearchView, EmployeeFilterView
app_name = 'app3_employee_management'
urlpatterns = [
    path('employee_management/add_employee',EmployeeAdd.as_view(),name="add_employee"),
    path('employee_management/employee_delete/<str:u_id>',EmployeeDelete.as_view(),name="employee_delete"),
    path('employee_management/edit_employee/<str:u_id>',EmployeeEdit.as_view(),name="edit_employee"),
    path('employee_management/employee_documents/<str:u_id>',EmployeeDocumentsAdd.as_view(),name="employee_documents"),
    path('employee_management/employee_document_delete/<str:d_id>',EmployeeDocumentsDelete.as_view(),name="employee_document_delete"),
    path('employee_management/employee_search',EmployeeSearchView.as_view(),name="employee_search"),
    path('employee_management/employee_filter/<str:filter_name>',EmployeeFilterView.as_view(),name="employee_filter"),
]