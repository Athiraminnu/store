from django.http import HttpResponse
from django.shortcuts import render
from .models import Department


def clghome(request):
    var = Department.objects.all()

    details = {
        'result': var}

    return render(request, "home.html", details)



