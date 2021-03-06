# Generated by Django 4.0.4 on 2022-06-25 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0050_allowedformats_alter_fieldofstudy_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='allowedformats',
            options={'verbose_name': 'فرمت', 'verbose_name_plural': 'فرمت ها'},
        ),
        migrations.AlterField(
            model_name='fieldofstudy',
            name='title',
            field=models.CharField(choices=[('Experimental_Science', 'علوم تجربی'), ('Mathematical_Physics', 'ریاضی فیزیک'), ('Liberal_Arts', 'علوم انسانی'), ('Software_Defined_Networking', 'شبکه و نرم افزار')], max_length=50, verbose_name='عنوان رشته تحصیلی'),
        ),
    ]
