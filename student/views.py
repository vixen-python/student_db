import json

from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from student.models import Student, Contact, Employer
from student.forms import StudentForm, ContactForm, AddressForm, EmployerForm


# Create your views here.
class LoginUserView(View):
    def post(self, request):
        output = {"message": ""}
        msg_success = 'You are logged in'
        msg_fail = 'I do not know you'

        request_json = json.loads(request.body)
        username = request_json.get('username', '').lower().strip()
        password = request_json.get('password')

        if username and password:
            if authenticate(username=username, password=password):
                output['message'] = msg_success
            else:
                output['message'] = msg_fail
        else:
            output['message'] = msg_fail

        return JsonResponse(output)


class StudentsView(ListView):
    template_name = 'students.html'
    model = Student


class StudentCreateView(CreateView):
    template_name = 'form.html'
    form_class = StudentForm
    success_url = reverse_lazy('index')
"""
    def form_valid(self, form):
        result = super().form_valid(form)
        Student.objects.create(
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            date_of_birth=form.cleaned_data['date_of_birth'],
            sex=form.cleaned_data['sex'],
            employment=form.cleaned_data['employment'],
            permanent_address=form.cleaned_data['permanent_address'],
            email=form.cleaned_data['email']
        )
        return result
"""


class StudentUpdateView(UpdateView):
    template_name = "form.html"
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('index')


class StudentDeleteView(DeleteView):
    template_name = "student_confirm_delete.html"
    model = Student
    success_url = reverse_lazy('index')


class ContactCreateView(CreateView):
    template_name = 'form.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')


class ContactUpdateView(UpdateView):
    template_name = "form.html"
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('index')


class AddressCreateView(CreateView):
    template_name = 'form.html'
    form_class = AddressForm
    success_url = reverse_lazy('index')


class EmployerView(ListView):
    template_name = 'employers.html'
    model = Employer


class EmployerCreateView(CreateView):
    template_name = "form.html"
    form_class = EmployerForm
    success_url = reverse_lazy('index')


class EmployerDeleteView(DeleteView):
    template_name = "employer_confirm_delete.html"
    model = Employer
    success_url = reverse_lazy('employer')


def student_info_by_id(request, requested_id):
    return render(
        request,
        template_name='student_info.html',
        context={'student': Student.objects.filter(id=requested_id).first()}
    )


def contact_info_by_id(request, requested_id):
    return render(
        request,
        template_name='contact_info.html',
        context={'contact': Contact.objects.filter(id=requested_id).first()}
    )


def address_info_by_id(request, requested_id):
    return render(
        request,
        template_name='address_info.html',
        context={'student': Student.objects.filter(id=requested_id).first()}
    )


def employer_info_by_id(request, requested_id):
    return render(
        request,
        template_name='employer_info.html',
        context={'employer': Employer.objects.filter(id=requested_id).first()}
    )