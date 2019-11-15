# Generated by Django 2.1.5 on 2019-11-10 17:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_auto_20191110_1717'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_auto_20191110_1647'),
    ]

    operations = [
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