# Generated by Django 3.2.9 on 2022-01-07 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0016_auto_20211229_1316'),
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='new', to='invoice_app.invoice')),
            ],
        ),
    ]
