from django.views.decorators.csrf import csrf_exempt
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

@csrf_exempt
def create_list(request):
    list = List(title=request.POST['title'])
    list.save()

    return HttpResponse('List created')


def update_list(request, list_id):
    list = get_object_or_404(List, pk=list_id)

    return HttpResponse()


def update_item(request, list_id, item_id):
    list = get_object_or_404(List, pk=list_id)

    return HttpResponse()