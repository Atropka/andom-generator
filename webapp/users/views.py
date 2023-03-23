import random

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import RandomNumber



@csrf_exempt
def generate_random_number(request):
    number = random.randint(1, 100)
    RandomNumber.objects.exclude(id=1).delete()
    RandomNumber.objects.create(number=number)
    data = {'number': number}
    return JsonResponse(data)



