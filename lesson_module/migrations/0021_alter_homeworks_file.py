# Generated by Django 4.0.4 on 2022-06-23 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_module', '0020_alter_homeworks_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeworks',
            name='file',
            field=models.FileField(upload_to='files/home_works', verbose_name='تکلیف ارسال شده'),
        ),
    ]
