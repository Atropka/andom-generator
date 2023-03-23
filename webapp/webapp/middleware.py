import random


class SetRandomSeedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        random.seed(42)  # Установка сида
        response = self.get_response(request)
        return response
