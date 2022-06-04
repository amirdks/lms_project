# Generated by Django 4.0.2 on 2022-05-06 10:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lessons', '0018_alter_base_title_alter_fieldofstudy_title'),
        ('lesson_module', '0006_alter_lesson_base'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان درس')),
                ('image', models.ImageField(upload_to='images/lessons', verbose_name='عکس درس')),
                ('slug', models.SlugField(verbose_name='آدرس در url')),
                ('is_active', models.BooleanField(verbose_name='فعال / غیرفعال')),
                ('base', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lessons.base', verbose_name='پایه')),
                ('field_of_study', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lessons.fieldofstudy', verbose_name='رشته')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='معلم')),
            ],
            options={
                'verbose_name': 'درس',
                'verbose_name_plural': 'درس ها',
            },
        ),
    ]
