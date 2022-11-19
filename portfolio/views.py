from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')

def list(request):
    return render(request, 'portfolio/list.html')