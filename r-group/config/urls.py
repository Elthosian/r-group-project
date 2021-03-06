"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from research_group import views



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^members/', views.members, name='members'),
    url(r'^articles/', views.articles, name='articles'),
    url(r'^projects/', views.projects, name='projects'),
    url(r'^conferences/', views.conferences, name='conferences'),

    url(r'^articles-(?P<id>\d+)/', views.article, name='article'),
    url(r'^conferences-(?P<id>\d+)/', views.conference, name='conference'),
    url(r'^projects-(?P<id>\d+)/', views.project, name='project'),

    url(r'^admin/', admin.site.urls),
    #url(r'^index/', views.index, name='index'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)