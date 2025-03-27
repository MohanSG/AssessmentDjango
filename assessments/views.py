from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# # Create your views here.

# def login(request):
#     template = loader.get_template("registration/login.html")
#     context = {'text' : 'This is some text!'}
#     return HttpResponse(template.render(context, request))

def index(request):
    print('This is the index')
    template = loader.get_template("assessments/index.html")
    context = {'text' : 'This is the assessment page index!'}
    return HttpResponse(template.render(context, request))