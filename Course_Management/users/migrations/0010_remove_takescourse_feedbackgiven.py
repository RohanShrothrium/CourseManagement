# Generated by Django 2.1.5 on 2019-11-16 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_remove_takescourse_courseid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='takescourse',
            name='FeedbackGiven',
        ),
    ]