from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, CreateView, UpdateView, DeleteView
from student.models import Student, Contact, Address, Employer
from student.forms import StudentForm, ContactForm, AddressForm, EmployerForm


# Create your views here.

class StudentsView(ListView):
    template_name = 'students.html'
    model = Student


class StudentCreateView(FormView):
    template_name = 'form.html'
    form_class = StudentForm
    success_url = reverse_lazy('index')

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


class AddressCreateView(FormView):
    template_name = 'form.html'
    form_class = AddressForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        Address.objects.create(
            street=form.cleaned_data['street'],
            house_number=form.cleaned_data['house_number'],
            city=form.cleaned_data['city'],
            zip_code=form.cleaned_data['zip_code'],
            country_iso3=form.cleaned_data['country_iso3']
        )
        return result


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