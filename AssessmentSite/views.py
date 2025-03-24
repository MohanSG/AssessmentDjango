from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def login(request):
    template = loader.get_template("registration/login.html")
    context = {'text' : 'This is the assessments page!'}
    return HttpResponse(template.render(context, request))
