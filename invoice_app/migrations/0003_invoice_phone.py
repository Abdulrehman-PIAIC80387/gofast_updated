# Generated by Django 2.1 on 2021-11-26 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0002_auto_20211127_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='phone',
            field=models.IntegerField(blank=True, default='0', null=True, verbose_name='Phone number'),
        ),
    ]
