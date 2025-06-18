from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def set_cookie(request, username):
    response = HttpResponse("Hello, %s!" % username)
    response.set_cookie('username', username)
    return response

def get_cookie(request):
    username = request.COOKIES['username']
    return HttpResponse(f'you are {username} right?')

