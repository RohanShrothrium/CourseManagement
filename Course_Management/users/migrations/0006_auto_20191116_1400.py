# Generated by Django 2.1.5 on 2019-11-16 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='Course',
        ),
        migrations.AddField(
            model_name='feedback',
            name='CourseID',
            field=models.CharField(default='', max_length=5),
        ),
    ]