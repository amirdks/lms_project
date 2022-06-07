# Generated by Django 4.0.2 on 2022-05-26 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_module', '0018_alter_lesson_teacher'),
        ('notification_module', '0002_alter_notification_options_notification_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='home_work',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_work', to='lesson_module.sethomework', verbose_name='مربوط به تکلیف'),
        ),
    ]