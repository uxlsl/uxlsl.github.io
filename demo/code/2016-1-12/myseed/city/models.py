from django.db import models


class People(models.Model):
    name = models.CharField(max_length=32, verbose_name="名字")
    age = models.IntegerField(verbose_name="年龄")
