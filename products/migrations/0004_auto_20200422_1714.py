# Generated by Django 3.0.5 on 2020-04-22 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200422_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='chips',
            field=models.ManyToManyField(blank=True, help_text='Select one or multiple chips...', to='products.Chip'),
        ),
    ]