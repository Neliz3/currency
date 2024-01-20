# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from currency_app.models import Rate, Source
from django.urls import get_resolver


def start_page(request):
    patterns = []
    for p in get_resolver().url_patterns:
        patterns.append(p.pattern)

    context = {
        'patterns': patterns,
    }

    return render(request, "index.html", context=context)


# GET id values from Rate model
def get_rate(request):
    result = []
    queryset = Rate.objects.all().values_list('id', flat=True)

    for q in queryset:
        result.append(q)

    context = {
        'model': 'Rate',
        'data': result,
    }
    return render(request, "rate.html", context=context)


# GET row from Rate model by ID
def get_rate_by_id(request, pk):
    # try:
    #     rate = Rate.objects.get(id=pk)
    # except Rate.DoesNotExist:
    #     raise Http404("Object does not exist.")

    rate = get_object_or_404(Rate, pk=pk)
    context = {
        'model': 'Rate',
        'rate': rate
    }
    return render(request, "rate.html", context=context)


# GET data from Source model
def get_source(request):

    result = []
    queryset = Source.objects.all().values_list('name', flat=True)

    for q in queryset:
        result.append(q)

    context = {
        'model': 'Source',
        'data': result
    }
    return render(request, "banks.html", context=context)


# GET row from Source model by ID
def get_source_by_id(request, pk):

    source = get_object_or_404(Source, pk=pk)
    context = {
        'model': 'Source',
        'bank': source
    }

    return render(request, "banks.html", context=context)
