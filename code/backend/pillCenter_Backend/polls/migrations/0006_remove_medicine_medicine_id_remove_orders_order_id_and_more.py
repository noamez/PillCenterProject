# Generated by Django 4.1.7 on 2023-03-23 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_rename_medcine_id_products_medicine_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicine',
            name='medicine_id',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='order_id',
        ),
        migrations.RemoveField(
            model_name='products',
            name='product_id',
        ),
        migrations.AlterField(
            model_name='inventory',
            name='machine_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.vending_machines'),
        ),
        migrations.AlterField(
            model_name='vending_machines',
            name='machine_id',
            field=models.IntegerField(),
        ),
    ]
