# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0015_auto_20160414_2211'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'verbose_name': 'Ticket', 'verbose_name_plural': 'Tickets', 'ordering': ('queue_id', 'milestone_id', 'priority', '-created'), 'get_latest_by': 'created'},
        ),
    ]
