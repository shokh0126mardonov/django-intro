from django.contrib import admin
from django.urls import path

from pages.views import home_wiew,home_about,home_contact,home_login,home_register,home_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_wiew),
    path('about/', home_about),
    path('contact/', home_contact),
    path('login/', home_login),
    path('register/', home_register),
    path('profile/', home_profile)
]

