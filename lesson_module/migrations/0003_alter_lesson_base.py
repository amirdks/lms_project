# Generated by Django 4.0.2 on 2022-05-06 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0013_alter_base_title_alter_fieldofstudy_title'),
        ('lesson_module', '0002_alter_lesson_base'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='base',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lessons.base', verbose_name='پایه2'),
        ),
    ]