# Generated by Django 4.0.2 on 2022-05-07 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_module', '0014_delete_nmd'),
    ]

    operations = [
        migrations.AddField(
            model_name='sethomework',
            name='finished',
            field=models.BooleanField(default=False, verbose_name='به اتمام رسیده'),
        ),
    ]