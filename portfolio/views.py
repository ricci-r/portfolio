from django.shortcuts import get_object_or_404, render

from .models import Category, Portfolio, Technology


def index(request):
    return render(request, 'home/index.html')

def list(request):
    portfolios = Portfolio.objects.all()
    categories = Category.objects.all()
    technologies = Technology.objects.all()
    is_published = True

    context = {
        'portfolios': portfolios,
        'categories': categories,
        'technologies': technologies,
    }

    return render(request, 'portfolio/list.html', context)

def detail(request, detail_id):
    portfolio = get_object_or_404(Portfolio, id=detail_id)
    tech = Technology.objects.all()

    context = {
        'portfolio' : portfolio,
        'tech' : tech,
    }

    return render(request, 'portfolio/detail.html', context)