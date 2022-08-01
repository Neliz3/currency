from django.http import HttpResponse
from django.shortcuts import render
#from currency_app.utils import generate_address as gd


# def generate_address(request):
#     address = gd()
#     return HttpResponse(address)


def get_text(request):
    line = 'Hello world!'
    return HttpResponse(line)
