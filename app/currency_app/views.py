from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
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
