# Generated by Django 4.1.7 on 2023-03-22 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_medicine_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='medicine_name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
