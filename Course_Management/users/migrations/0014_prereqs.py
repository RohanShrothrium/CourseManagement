# Generated by Django 2.1.5 on 2019-11-19 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20191116_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prereqs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseID', models.CharField(default='', max_length=5)),
                ('PrereqID', models.CharField(default='', max_length=5)),
            ],
        ),
    ]
