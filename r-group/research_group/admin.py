from django.contrib import admin

from .models import Person
from .models import Item
from .models import Project
from .models import Ownership
from .models import Conference
from .models import Article

#Registro de modelos.

admin.site.register(Person)
admin.site.register(Item)
admin.site.register(Ownership)
admin.site.register(Project)
admin.site.register(Conference)
admin.site.register(Article)

