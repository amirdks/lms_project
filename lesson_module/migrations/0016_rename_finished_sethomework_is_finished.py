# Generated by Django 4.0.2 on 2022-05-07 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_module', '0015_sethomework_finished'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sethomework',
            old_name='finished',
            new_name='is_finished',
        ),
    ]
