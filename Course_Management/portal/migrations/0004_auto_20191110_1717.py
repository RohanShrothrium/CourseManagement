# Generated by Django 2.1.5 on 2019-11-10 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_project_takesproject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='takesproject',
            name='Project',
        ),
        migrations.RemoveField(
            model_name='takesproject',
            name='Student',
        ),
        migrations.DeleteModel(
            name='TakesProject',
        ),
    ]
