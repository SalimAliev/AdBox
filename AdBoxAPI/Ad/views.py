from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
# Create your views here.


def Ad_View(request):
    # return JsonResponse({'response': 'Value1'})
    return HttpResponse('<h1>что-то</h1>')

