# Generated by Django 2.1.5 on 2019-11-10 17:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portal', '0002_classroom_instructor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProjectID', models.CharField(default='', max_length=5)),
                ('InstID', models.CharField(default='', max_length=5)),
                ('Title', models.TextField()),
                ('Description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TakesProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Performance', models.TextField()),
                ('Feedback', models.TextField()),
                ('Project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Project')),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]