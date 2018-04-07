# Generated by Django 2.0.3 on 2018-04-07 13:32

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_auto_20180407_1858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='section',
        ),
        migrations.AddField(
            model_name='student',
            name='join_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentenroll',
            name='section',
            field=models.ForeignKey(default=datetime.datetime(2018, 4, 7, 13, 32, 52, 782384, tzinfo=utc), help_text='Assign Class_code', on_delete=django.db.models.deletion.CASCADE, to='student.Section'),
            preserve_default=False,
        ),
    ]