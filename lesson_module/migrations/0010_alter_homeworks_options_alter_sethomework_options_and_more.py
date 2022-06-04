# Generated by Django 4.0.2 on 2022-05-06 12:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lesson_module', '0009_sethomework_homeworks'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homeworks',
            options={'verbose_name': 'تکلیف ارسال شده', 'verbose_name_plural': 'تکالیف ارسال شده'},
        ),
        migrations.AlterModelOptions(
            name='sethomework',
            options={'verbose_name': 'تکلیف قرار داده شده', 'verbose_name_plural': 'تکالیف قرار داده شده'},
        ),
        migrations.AlterField(
            model_name='sethomework',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='معلم'),
        ),
    ]
