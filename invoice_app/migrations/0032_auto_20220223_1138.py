# Generated by Django 3.0.7 on 2022-02-23 06:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0031_auto_20220223_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='travel_time1',
            field=models.TimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Time Travel'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='travel_time2',
            field=models.TimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Time Travel'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='travel_time3',
            field=models.TimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Time Travel'),
        ),
    ]
