"""students_db URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from student.views import student_info_by_id, StudentsView, StudentCreateView, contact_info_by_id, address_info_by_id, \
    ContactCreateView, AddressCreateView, EmployerCreateView, StudentUpdateView, ContactUpdateView, StudentDeleteView, \
    EmployerView, employer_info_by_id, EmployerDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StudentsView.as_view(), name='index'),
    path('employer/', EmployerView.as_view(), name='employer'),
    path('student/<int:requested_id>', student_info_by_id, name='student_card'),
    path('student/contacts/<int:requested_id>', contact_info_by_id, name='contact_card'),
    path('student/address/<int:requested_id>', address_info_by_id, name='address_card'),
    path('employer/<int:requested_id>', employer_info_by_id, name='employer_card'),
    path('student/create/', StudentCreateView.as_view(), name='student_create'),
    path('student/contact/create/', ContactCreateView.as_view(), name='contact_create'),
    path('address/create/', AddressCreateView.as_view(), name='address_create'),
    path('employers/create/', EmployerCreateView.as_view(), name='employer_create'),
    path('student/update/<pk>/', StudentUpdateView.as_view(), name='student_update'),
    path('student/contact/update/<pk>/', ContactUpdateView.as_view(), name='contact_update'),
    path('student/delete/<pk>/', StudentDeleteView.as_view(), name='student_delete'),
    path('employer/delete/<pk>/', EmployerDeleteView.as_view(), name='employer_delete')
]
