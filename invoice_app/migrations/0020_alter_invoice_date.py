# Generated by Django 3.2.9 on 2022-01-07 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0019_auto_20220107_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Travel Date'),
        ),
    ]
