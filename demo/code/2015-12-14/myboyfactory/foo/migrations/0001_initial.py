# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('firstname', models.CharField(max_length=32)),
                ('lastname', models.CharField(max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
