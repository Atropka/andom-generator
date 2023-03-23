from django.urls import path, include

from .views import generate_random_number

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('generate_random_number/', generate_random_number, name='generate_random_number'),

]