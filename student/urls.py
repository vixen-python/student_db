from django.urls import path

from student.views import student_info_by_id, contact_info_by_id, address_info_by_id, \
    StudentCreateView, ContactCreateView, StudentUpdateView, ContactUpdateView, StudentDeleteView, StudentsView

app_name = 'student'

urlpatterns = [
    path('', StudentsView.as_view(), name='student_list'),
    path('<int:requested_id>/', student_info_by_id, name='student_card'),
    path('contacts/<int:requested_id>', contact_info_by_id, name='contact_card'),
    path('address/<int:requested_id>', address_info_by_id, name='address_card'),
    path('create/', StudentCreateView.as_view(), name='student_create'),
    path('contact/create/', ContactCreateView.as_view(), name='contact_create'),
    path('update/<pk>/', StudentUpdateView.as_view(), name='student_update'),
    path('contact/update/<pk>/', ContactUpdateView.as_view(), name='contact_update'),
    path('delete/<pk>/', StudentDeleteView.as_view(), name='student_delete'),
]