from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


def Ad_View(request):
    return JsonResponse({'response': 'Value1'})