from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse('hello world!')


def login(request):
    name = request.GET.get('uname', '')
    passwd = request.GET.get('passwd', '')
    if name == 'gss' and passwd == '123':
        return HttpResponse('login success!')
    return HttpResponse('login failed!')
