from django.shortcuts import render
from django.http import HttpResponse

from .models import WelcomeMessage


# Create your views here.


def home(request):
    wm = WelcomeMessage.objects.get(id=1)
    context = {
        "message": wm.message,
    }
    return render(request, "home.html", context)

