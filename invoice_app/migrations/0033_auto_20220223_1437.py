# Generated by Django 3.0.7 on 2022-02-23 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0032_auto_20220223_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='Travel_date1',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Travel Date'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='Travel_date2',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Travel Date'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='Travel_date3',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Travel Date'),
        ),
    ]
