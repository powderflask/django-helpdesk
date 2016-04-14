# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import helpdesk.models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0014_auto_20160220_0625'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'get_latest_by': 'created', 'ordering': ('milestone_id', 'priority', '-created'), 'verbose_name_plural': 'Tickets', 'verbose_name': 'Ticket'},
        ),
        migrations.AlterField(
            model_name='attachment',
            name='file',
            field=models.FileField(max_length=1000, upload_to=helpdesk.models.attachment_path, validators=[helpdesk.models.validate_file_extension], verbose_name='File'),
        ),
    ]
