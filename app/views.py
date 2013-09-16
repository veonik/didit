from django.shortcuts import render
from django.http import Http404

from app.models import List


def index(request):
    lists = List.objects.all()
    context = {'lists': lists}

    return render(request, 'app/index.html', context)


def detail(request, list_id):
    try:
        list = List.objects.get(id=list_id)
    except List.DoesNotExist:
        raise Http404

    return render(request, 'app/detail.html', {'list': list})

