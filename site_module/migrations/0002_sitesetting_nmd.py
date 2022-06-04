# Generated by Django 4.0.2 on 2022-05-06 10:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('site_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='nmd',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
