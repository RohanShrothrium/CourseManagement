# Generated by Django 2.1.5 on 2019-11-10 17:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_auto_20191110_1717'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_takesproject'),
    ]

    operations = [
        migrations.CreateModel(
            name='TakesCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year', models.CharField(max_length=4)),
                ('Sem', models.CharField(max_length=6)),
                ('Grade', models.CharField(default='OG', max_length=2)),
                ('Feedback', models.TextField()),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Course')),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]