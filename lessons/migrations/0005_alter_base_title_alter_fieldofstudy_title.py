# Generated by Django 4.0.2 on 2022-05-06 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0004_alter_base_title_alter_fieldofstudy_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base',
            name='title',
            field=models.CharField(choices=[('paye_12', 'پایه دوازدهم'), ('paye_11', 'پایه یازدهم'), ('paye_10', 'پایه دهم')], default='paye_10', max_length=50, verbose_name='عنوان پایه'),
        ),
        migrations.AlterField(
            model_name='fieldofstudy',
            name='title',
            field=models.CharField(choices=[('Software_Defined_Networking', 'شبکه و نرم افزار'), ('Liberal_Arts', 'علوم انسانی'), ('Experimental_Science', 'علوم تجربی'), ('Mathematical_Physics', 'ریاضی فیزیک')], max_length=50, verbose_name='عنوان رشته تحصیلی'),
        ),
    ]