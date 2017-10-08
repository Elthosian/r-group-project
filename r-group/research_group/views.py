from django.shortcuts import render

def home(request):
    articles = Article.objects.all()
    return render(request, 'home.html', {'articles': articles})


def about(request):
    return render(request, 'about.html')


def index(request):
    return render(request, 'index.html')