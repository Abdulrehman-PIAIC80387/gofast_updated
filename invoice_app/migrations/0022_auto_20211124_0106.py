# Generated by Django 2.1 on 2021-11-23 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0021_auto_20211124_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='service_name',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='invoice_app.services'),
        ),
    ]
