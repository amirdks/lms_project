# Generated by Django 4.0.4 on 2022-06-25 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_module', '0029_alter_homeworks_file'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homeworkfiles',
            options={'verbose_name': 'فایل ارسال شده', 'verbose_name_plural': 'فایل های ارسال شده'},
        ),
        migrations.RemoveField(
            model_name='homeworks',
            name='file',
        ),
        migrations.AddField(
            model_name='homeworks',
            name='message',
            field=models.TextField(blank=True, null=True, verbose_name='پیام به معلم'),
        ),
    ]