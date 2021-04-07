from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def get_order(request, id=None):
    message = f'You submitted ID: {id}'
    return HttpResponse(message)