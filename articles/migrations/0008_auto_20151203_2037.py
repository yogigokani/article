# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_article_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='image',
            new_name='hero_image',
        ),
        migrations.AddField(
            model_name='article',
            name='optional_image',
            field=models.ImageField(null=True, upload_to=b'uploads', blank=True),
        ),
    ]
