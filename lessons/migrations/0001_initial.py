# Generated by Django 4.0.2 on 2022-05-06 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('paye_11', 'پایه یازدهم'), ('paye_12', 'پایه دوازدهم'), ('paye_10', 'پایه دهم')], default='paye_10', max_length=50, verbose_name='عنوان پایه')),
                ('base_number', models.IntegerField(default=10, editable=False, verbose_name='عدد پایه')),
            ],
            options={
                'verbose_name': 'پایه',
                'verbose_name_plural': 'پایه ها',
            },
        ),
        migrations.CreateModel(
            name='FieldOfStudy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Liberal_Arts', 'علوم انسانی'), ('Software_Defined_Networking', 'شبکه و نرم افزار'), ('Mathematical_Physics', 'ریاضی فیزیک'), ('Experimental_Science', 'علوم تجربی')], max_length=50, verbose_name='عنوان رشته تحصیلی')),
            ],
            options={
                'verbose_name': 'رشته',
                'verbose_name_plural': 'رشته ها',
            },
        ),
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان درس')),
                ('image', models.ImageField(upload_to='images/lessons', verbose_name='عکس درس')),
                ('slug', models.SlugField(verbose_name='آدرس در url')),
                ('is_active', models.BooleanField(verbose_name='فعال / غیرفعال')),
                ('base', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.base', verbose_name='پایه')),
                ('field_of_study', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lessons.fieldofstudy', verbose_name='رشته')),
            ],
            options={
                'verbose_name': 'درس',
                'verbose_name_plural': 'درس ها',
            },
        ),
    ]
