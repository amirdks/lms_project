# Generated by Django 4.0.4 on 2022-06-25 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0052_alter_base_title_alter_fieldofstudy_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldofstudy',
            name='title',
            field=models.CharField(choices=[('Liberal_Arts', 'علوم انسانی'), ('Experimental_Science', 'علوم تجربی'), ('Mathematical_Physics', 'ریاضی فیزیک'), ('Software_Defined_Networking', 'شبکه و نرم افزار')], max_length=50, verbose_name='عنوان رشته تحصیلی'),
        ),
    ]
