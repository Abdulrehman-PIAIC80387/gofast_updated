# Generated by Django 2.1 on 2021-11-23 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0005_auto_20211123_0048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='balance',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='invoice_date',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='invoice_type',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='last_updated',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='line_five',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='line_five_quantity',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='line_five_total_price',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='line_five_unit_price',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='line_four',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='line_four_quantity',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='line_four_total_price',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='line_four_unit_price',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='line_one',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='line_one_quantity',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='line_one_total_price',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='line_one_unit_price',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='line_three',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='line_three_quantity',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='line_three_total_price',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='line_three_unit_price',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='line_two',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='line_two_quantity',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='line_two_total_price',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='line_two_unit_price',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='name',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='paid',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='total',
        ),
        migrations.AddField(
            model_name='invoice',
            name='Destination',
            field=models.CharField(blank=True, default='', max_length=120, null=True, verbose_name='Destination'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='pending',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Pending '),
        ),
        migrations.AddField(
            model_name='invoice',
            name='profit',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Profit'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='purchase',
            field=models.CharField(blank=True, default='', max_length=120, null=True, verbose_name='Purchase Name'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='purchase_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Purchase Price'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='received',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Received'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='sale_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Sale Price'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='service_name',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='invoice_app.services'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='travel_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
