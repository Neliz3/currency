from django.http import HttpResponse
from django.shortcuts import render
from currency_app.models import Rate


def hello_world(request):
    return HttpResponse("Hello!")


def get_data(request):
    result = []
    queryset = Rate.objects.all().values_list('id', flat=True)

    for q in queryset:
        result.append(q)

    context = {
        'model': 'Rate',
        'data': result,
    }
    return render(request, "index.html", context=context)


def get_row(request):
    id_ = request.GET['id']
    rate = Rate.objects.get(id=id_)

    context = {
        'model': 'Rate',
        'object': rate
    }
    return render(request, "get_row.html", context=context)
