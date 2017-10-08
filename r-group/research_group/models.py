from django.db import models

class Person(models.Model):
    PREFIXES = (
        ('PHD', 'PhD.'),
        ('MSC', 'MSc.'),
        ('ENG', 'Ing.'),
        ('MAL', 'Sr.'),
        ('FEM', 'Sra.')
    )
    name = models.CharField("Nombre", max_length=150)
    prefix = models.CharField("Prefijo", max_length=3, choices=PREFIXES,
                              default=None, blank=True, null=True,
                              )
    title = models.TextField("Títulos")
    photo_url = models.URLField("Fotografía", max_length=250, default=None, blank=True, null=True)

    def __str__(self):
        if self.prefix:
            return self.get_prefix_display() + ' ' + self.name
        else:
            return self.name


class Item(models.Model):
    name = models.CharField(max_length=250)
    abstract = models.TextField(default=None, blank=True, null=True)
    date = models.DateField(default=None, blank=True, null=True)
    information = models.TextField(default=None, blank=True, null=True)
    image_url = models.CharField(max_length=250, default=None,
                                 blank=True, null=True)
    source = models.TextField(default=None, blank=True, null=True)
    main_project = models.ForeignKey('self', default=None, blank=True, null=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    item = models.OneToOneField(Item)

    def __str__(self):
        return self.item.name


class Article(models.Model):
    item = models.OneToOneField(Item)

    def __str__(self):
        return self.item.name


class Conference(models.Model):
    item = models.OneToOneField(Item)
    place = models.TextField()
    end_date = models.DateField()

    def __str__(self):
        return self.item.name


class Ownership(models.Model):
    person=models.ForeignKey(Person, on_delete=models.CASCADE)
    item=models.ForeignKey(Item, on_delete=models.CASCADE)
    main=models.BooleanField()

    def __str__(self):
        if self.main:
            return self.person.name + " es autor principal en " + self.item.name
        else:
            return self.person.name + " es autor principal en " + self.item.name



