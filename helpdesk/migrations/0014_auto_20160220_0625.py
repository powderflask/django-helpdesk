# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0013_auto_20160220_0308'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='milestone',
            options={'verbose_name_plural': 'Milestones', 'verbose_name': 'Milestone', 'ordering': ('id',)},
        ),
        migrations.AlterField(
            model_name='ticket',
            name='milestone',
            field=models.ForeignKey(to='helpdesk.Milestone', null=True, on_delete=django.db.models.deletion.SET_NULL, verbose_name='Milestone', blank=True),
        ),
    ]
