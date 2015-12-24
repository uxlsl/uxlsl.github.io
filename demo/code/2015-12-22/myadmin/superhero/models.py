from __future__ import unicode_literals

from django.db import models


class SuperHero(models.Model):
    name = models.CharField(max_length=32, default="hero")
    added_on = models.DateTimeField(auto_now_add=True)
    Address = models.ManyToManyField('Address')

    def __str__(self):
        return "{0} - {1:%Y-%m-%d %H:%M:%S}".format(self.name,
                                                    self.added_on)

    def get_absolute_url(self):
        return reverse('superhero.views.details', args=[self.id])


class Wife(models.Model):
    superhero = models.ForeignKey(SuperHero)
    name = models.CharField(max_length=32)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0} - {1:%Y-%m-%d %H:%M:%S}".format(self.name,
                                                    self.added_on)


class Address(models.Model):
    city = models.CharField(max_length=32)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0} - {1:%Y-%m-%d %H:%M:%S}".format(self.city,
                                                    self.added_on
                                                    )
