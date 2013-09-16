from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from app.models import List


def index(request):
    lists = List.objects.all()
    context = {'lists': lists}

    return render(request, 'app/index.html', context)


def detail(request, list_id):
    list = get_object_or_404(List, pk=list_id)

    return render(request, 'app/detail.html', {'list': list})


def create_list(request):
    list = List(title=request.POST['title'])
    list.save()

    return HttpResponse('List created')


def create_item(request, list_id):
    list = get_object_or_404(List, pk=list_id)
    ticket = list.ticket_set.create(title=request.POST['title'], description=request.POST['description'])
    ticket.save()

    return HttpResponse()


def close_item(request, list_id, item_id):
    list = get_object_or_404(List, pk=list_id)

    return HttpResponse()