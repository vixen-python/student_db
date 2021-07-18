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
from django.urls import path, include
import student.urls
from student.views import AddressCreateView, EmployerCreateView, \
    EmployerView, employer_info_by_id, EmployerDeleteView, LoginUserView, IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include(student.urls, namespace='student')),
    path('', IndexView.as_view(), name='index'),
    path('employer/', EmployerView.as_view(), name='employer'),
    path('employer/<int:requested_id>', employer_info_by_id, name='employer_card'),
    path('address/create/', AddressCreateView.as_view(), name='address_create'),
    path('employers/create/', EmployerCreateView.as_view(), name='employer_create'),
    path('employer/delete/<pk>/', EmployerDeleteView.as_view(), name='employer_delete'),
    path('user/login/', LoginUserView.as_view(), name='users_login')
]
