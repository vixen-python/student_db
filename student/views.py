from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from student.models import Student


# Create your views here.
def hello(request):
    return HttpResponse('Hello, World!', status=404)


def hello_user(request, user_id):
    usr_msg = request.GET.get('usr_msg', '')
    if usr_msg:
        usr_msg = f'Message from you: "{usr_msg}"'
    return HttpResponse(f'Hello, user with ID <{user_id}>! {usr_msg}', status=200)


def hello_user_msg(request, user_id, msg):
    return HttpResponse(
        f'Hello, user with ID <{user_id}>! Your message is: "{msg}"',
        status=200
    )


def hello_json(request, user_id):
    output_data = {
        'server_msg': f'Hello, user with ID <{user_id}>!',
        'user_msg': request.GET.get('usr_msg', '')
    }
    return JsonResponse(output_data)


def hello_view(request):
    # <protocol>://<hostname>/<url>/?<params>
    s1 = request.GET.get('s1', '')
    return render(
        request,
        template_name='hello.html',
        context={'adjectives': [s1, 'beautiful', 'wonderful']}
    )


def students_view(request):
    return render(
        request,
        template_name='students.html',
        context={'students': Student.objects.all()}
    )


def student_info_by_id(request, requested_id):
    return render(
        request,
        template_name='student_info.html',
        context={'student': Student.objects.filter(id=requested_id).first()}
    )