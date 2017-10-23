from django.shortcuts import render
from .models import Person, Article, Conference, Project

def about(request):
    return render(request, 'about.html')

def members(request):
    persons = Person.objects.all()
    return render(request, 'members.html', {'members': persons})

def articles(request):
    articles=Article.objects.order_by('-item__date')
    return render(request, 'articles.html', {'articles': articles})

def conferences(request):
    conferences=Conference.objects.order_by('-item__date')
    return render(request, 'conferences.html', {'conferences': conferences})

def projects(request):
    projects=Conference.objects.order_by('-item__date')
    return render(request, 'projects.html', {'projects': projects})

def index(request):
    articles=Article.objects.order_by('-item__date')[:3]
    conferences=Conference.objects.order_by('-item__date')[:3]
    projects=Project.objects.order_by('-item__date')[:3]
    return render(request, 'index.html', {
        'articles':articles,
        'conferences':conferences,
        'projects':projects
    })

