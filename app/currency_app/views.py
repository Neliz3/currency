from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from currency_app.models import Rate, Source


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


def get_row(request, pk):
    # try:
    #     rate = Rate.objects.get(id=pk)
    # except Rate.DoesNotExist:
    #     raise Http404("Object does not exist.")

    rate = get_object_or_404(Rate, pk=pk)
    context = {
        'model': 'Rate',
        'object': rate
    }
    return render(request, "get_row.html", context=context)


def get_source(request):

    result = []
    queryset = Source.objects.all().values_list('name', flat=True)

    for q in queryset:
        result.append(q)

    context = {
        'model': 'Source',
        'object': result
    }
    return render(request, "banks.html", context=context)


def get_source_by_id(request, pk):

    source = get_object_or_404(Source, pk=pk)
    context = {
        'model': 'Source',
        'bank': source
    }

    return render(request, "banks.html", context=context)
