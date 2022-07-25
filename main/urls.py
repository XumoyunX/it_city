from django.urls import path
from main.views import *

urlpatterns = [
    path('', index, name='index'),
    path('course/', course, name='course'),
    path('teacher/', teacher, name='teacher'),
    path('new/', new, name='new'),
    path('contact/', contact, name='contact')
]
