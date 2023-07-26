from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.
from django.shortcuts import render
from .notifications import show_notification

def my_view(request):
    # Ваш код представления
    show_notification(request, 'Пример уведомления', messages.SUCCESS)
    return render(request, 'main.html')