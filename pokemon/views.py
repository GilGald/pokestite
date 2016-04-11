from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests


def index(request,q):    
    img="http://pokeapi.co/media/img/"+q+".png"    
    url="http://pokeapi.co/media/img/"+q+".png"    
    
    template = loader.get_template('pokemonTemplate.html')

    context={'name':'',
    		'img':'',
    		'url':''}
    return HttpResponse(template.render(context,request))    