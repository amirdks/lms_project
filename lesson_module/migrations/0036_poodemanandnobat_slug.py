# Generated by Django 4.0.4 on 2022-07-09 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_module', '0035_homeworks_score_sethomework_score_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='poodemanandnobat',
            name='slug',
            field=models.SlugField(blank=True, max_length=30, null=True, verbose_name='عنوان در url'),
        ),
    ]
