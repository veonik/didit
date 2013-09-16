from django.http import HttpResponse
from django.template import RequestContext, loader

from app.models import List


def index(request):
    lists = List.objects.all()
    template = loader.get_template('app/index.html')
    context = RequestContext(request, {
        'lists': lists,
    })

    return HttpResponse(template.render(context))