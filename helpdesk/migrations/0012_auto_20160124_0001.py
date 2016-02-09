# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0011_admin_related_improvements'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='ticket_type',
            field=models.IntegerField(choices=[(1, 'Issue / Bug'), (2, 'Enhancement'), (3, 'New Feature'), (4, 'Task / To Do'), (5, 'Training')], verbose_name='Status', default=1),
        ),
        migrations.AlterField(
            model_name='followup',
            name='new_status',
            field=models.IntegerField(help_text='If the status was changed, what was it changed to?', verbose_name='New Status', null=True, choices=[(1, 'Open'), (2, 'Reopened'), (3, 'Resolved'), (4, 'Closed'), (5, 'Duplicate'), (6, "Won't Fix")], blank=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.IntegerField(choices=[(1, 'Open'), (2, 'Reopened'), (3, 'Resolved'), (4, 'Closed'), (5, 'Duplicate'), (6, "Won't Fix")], verbose_name='Status', default=1),
        ),
    ]
