# Generated by Django 4.1.7 on 2023-04-27 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_orders_qr_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='qr_codes'),
        ),
    ]
