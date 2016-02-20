# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0012_auto_20160124_0001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(verbose_name='Title', max_length=100)),
                ('slug', models.SlugField(verbose_name='Slug', help_text="This slug is used when building ticket ID's. Once set, try not to change it.", unique=True)),
                ('is_active', models.BooleanField(verbose_name='Active?', help_text='In-active milestones will not be visible via the ticketing system.', default=True)),
            ],
            options={
                'verbose_name': 'Milestone',
                'ordering': ('title',),
                'verbose_name_plural': 'Milestones',
            },
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticket_type',
            field=models.IntegerField(verbose_name='Ticket Type', default=1, choices=[(1, 'Issue / Bug'), (2, 'Enhancement'), (3, 'New Feature'), (4, 'Task / To Do'), (5, 'Training')]),
        ),
        migrations.AddField(
            model_name='ticket',
            name='milestone',
            field=models.ForeignKey(verbose_name='Milestone', to='helpdesk.Milestone', null=True, blank=True),
        ),
    ]
