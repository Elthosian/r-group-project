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

def article(request, id):
    article=Article.objects.get(pk=id)
    authors=Person.objects.filter(ownership__item__pk=article.item.pk).order_by('ownership__main')
    authors_txt=', '.join([author.__str__() for author in authors])
    return render(request, 'article.html', {'article':article, 'authors':authors_txt})

def conferences(request):
    conferences=Conference.objects.order_by('-item__date')
    return render(request, 'conferences.html', {'conferences': conferences})


def conference(request, id):
    conference=Conference.objects.get(pk=id)
    authors=Person.objects.filter(ownership__item__pk=conference.item.pk).order_by('ownership__main')
    authors_txt=', '.join([author.__str__() for author in authors])
    return render(request, 'conference.html', {'conference':conference, 'authors':authors_txt})


def projects(request):
    projects=Project.objects.order_by('-item__date')
    return render(request, 'projects.html', {'projects': projects})

def project(request, id):
    project=Project.objects.get(pk=id)
    authors=Person.objects.filter(ownership__item__pk=project.item.pk).order_by('ownership__main')
    authors_txt=', '.join([author.__str__() for author in authors])
    return render(request, 'project.html', {'project':project, 'authors':authors_txt})

def index(request):
    articles=Article.objects.order_by('-item__date')[:3]
    conferences=Conference.objects.order_by('-item__date')[:3]
    projects=Project.objects.order_by('-item__date')[:3]
    return render(request, 'index.html', {
        'articles':articles,
        'conferences':conferences,
        'projects':projects
    })

