from django.shortcuts import render
from student.models import Student
from django.views.generic import ListView


# Create your views here.

class StudentsView(ListView):
    template_name = 'students.html'
    model = Student


def student_info_by_id(request, requested_id):
    return render(
        request,
        template_name='student_info.html',
        context={'student': Student.objects.filter(id=requested_id).first()}
    )