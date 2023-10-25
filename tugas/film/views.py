from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
def horor(request):
    template = loader.get_template('horor.html')
    return HttpResponse(template.render())
def romance(request):
    template = loader.get_template('romance.html')
    return HttpResponse(template.render())
def action(request):
    template = loader.get_template('action.html')
    return HttpResponse(template.render())


# Create your views here.
