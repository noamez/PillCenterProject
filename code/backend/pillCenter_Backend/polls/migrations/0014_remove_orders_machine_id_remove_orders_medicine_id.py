# Generated by Django 4.1.7 on 2023-04-20 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_alter_orders_machine_id_alter_orders_medicine_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='machine_id',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='medicine_id',
        ),
    ]
