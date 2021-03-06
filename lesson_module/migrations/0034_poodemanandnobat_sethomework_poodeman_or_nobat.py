# Generated by Django 4.0.4 on 2022-06-26 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_module', '0033_lesson_poodeman_or_nobat_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PoodemanAndNobat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='نام')),
                ('type', models.CharField(choices=[('poodeman', 'پودمانی'), ('nobat', 'نوبتی')], max_length=15, verbose_name='نوع')),
            ],
            options={
                'verbose_name': 'پودمان و نوبت',
                'verbose_name_plural': 'پودمان ها و نوبت ها',
            },
        ),
        migrations.AddField(
            model_name='sethomework',
            name='poodeman_or_nobat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lesson_module.poodemanandnobat', verbose_name='پودمان یا نوبت'),
        ),
    ]
