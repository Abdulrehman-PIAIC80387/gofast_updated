# Generated by Django 2.1 on 2021-11-22 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0004_alter_services_service_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
