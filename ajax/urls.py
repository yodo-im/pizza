# ajax/urls.py
from django.urls import path, include
from .views import contact_form

urlpatterns = [
    path('contact-form/', contact_form, name='contact_form')
]