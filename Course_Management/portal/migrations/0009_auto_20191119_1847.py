# Generated by Django 2.1.5 on 2019-11-19 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0008_prereqs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prereqs',
            name='CourseID',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='prereqs',
            name='PrereqID',
            field=models.CharField(max_length=5),
        ),
    ]