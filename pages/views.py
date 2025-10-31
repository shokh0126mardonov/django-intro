from django.http import HttpResponse

from .frontend import home,about,contact,profile

def home_wiew(x):
    return HttpResponse(
        home
    )

def home_about(x):
    return HttpResponse(
        about
    )

def home_contact(x):
    return HttpResponse(
        contact
    )

def home_login(x):
    return HttpResponse(
        'home page'
    )

def home_register(x):
    return HttpResponse(
        'home page'
    )

def home_profile(x):
    return HttpResponse(
        profile
    )

