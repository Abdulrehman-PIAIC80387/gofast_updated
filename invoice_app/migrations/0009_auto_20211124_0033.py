# Generated by Django 2.1 on 2021-11-23 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0008_auto_20211124_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_number',
            field=models.IntegerField(blank=True, default=''),
        ),
    ]
