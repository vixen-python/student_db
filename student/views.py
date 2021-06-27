from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


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
