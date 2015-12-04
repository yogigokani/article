# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20151202_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default=b'c:/django/myarticle/articles/static/img/work.jpg', upload_to=b'c:/django/myarticle/articles/static/img'),
        ),
    ]
