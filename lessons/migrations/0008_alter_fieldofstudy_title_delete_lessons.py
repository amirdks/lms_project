# Generated by Django 4.0.2 on 2022-05-06 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0007_alter_base_title_alter_fieldofstudy_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldofstudy',
            name='title',
            field=models.CharField(choices=[('Liberal_Arts', 'علوم انسانی'), ('Experimental_Science', 'علوم تجربی'), ('Software_Defined_Networking', 'شبکه و نرم افزار'), ('Mathematical_Physics', 'ریاضی فیزیک')], max_length=50, verbose_name='عنوان رشته تحصیلی'),
        ),
        migrations.DeleteModel(
            name='Lessons',
        ),
    ]