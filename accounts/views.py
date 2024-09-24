from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

# Create your views here.
def index(request):
    current_time = timezone.now()
    return HttpResponse("Hello, world. You're at the accounts index. Current server time: " + str(current_time))
