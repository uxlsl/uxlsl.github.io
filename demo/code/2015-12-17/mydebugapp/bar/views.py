from django.http import JsonResponse
from .models import People


def hello(request):
    p = People.objects.all().count()
    print(p)
    return JsonResponse({"hello":123})
