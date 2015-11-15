# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SendSmsLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
                ('request_params', jsonfield.fields.JSONField()),
                ('response', jsonfield.fields.JSONField(null=True)),
                ('error', models.CharField(max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SmsAPIGate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=64)),
                ('url', models.URLField(max_length=256)),
                ('handler', models.CharField(default=b'common', max_length=32, choices=[(b'common', b'common'), (b'custom', b'custom')])),
            ],
        ),
        migrations.AddField(
            model_name='sendsmslog',
            name='api_gate',
            field=models.ForeignKey(related_name='log_records', to='sender.SmsAPIGate'),
        ),
    ]
