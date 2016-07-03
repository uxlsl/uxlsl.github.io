from django.shortcuts import render
from django.http.response import JsonResponse

from .models import Genre


def index(request):
    return render(request, 'index.html')


def genre_jstree(root, data=dict):
    if hasattr(data, '__call__'):
        data = data()
    data['text'] = root.name
    children = root.children.all()
    if len(children) > 0:
        data['children'] = []
        for n in children:
            data['children'].append(genre_jstree(n))
    return data


def genre_jstree_v(request):
    root = Genre.objects.first().get_root()
    return JsonResponse(genre_jstree(root))
