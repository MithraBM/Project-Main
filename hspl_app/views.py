from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

def home(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())
    
