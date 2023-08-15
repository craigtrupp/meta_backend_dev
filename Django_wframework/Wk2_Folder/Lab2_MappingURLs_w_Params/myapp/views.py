from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def drinks(request, drink_name):
    drinks = {
        'mocha': 'type of coffee', 
        'tea': 'type of beverage',
        'lemonade': 'type of refreshment',
        'arnold_palmer': 'mix of lemonade and tea'
    }
    choice_of_drink = drinks[drink_name]
    return HttpResponse(f'<h2>{drink_name}</h2><p>{choice_of_drink}</p>')
