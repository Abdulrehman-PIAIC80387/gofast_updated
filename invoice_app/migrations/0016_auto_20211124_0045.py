# Generated by Django 2.1 on 2021-11-23 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0015_auto_20211124_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_number',
            field=models.IntegerField(blank=True),
        ),
    ]
