# Generated by Django 3.0.5 on 2020-04-22 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200422_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chip',
            name='package',
            field=models.ManyToManyField(blank=True, default=None, help_text='Select one or multiple packages...', to='products.Package'),
        ),
        migrations.AlterField(
            model_name='chip',
            name='vendor',
            field=models.ManyToManyField(blank=True, default=None, help_text='Select one or multiple vendor locations', to='products.MfgLoc', verbose_name='Vendor Locations'),
        ),
        migrations.AlterField(
            model_name='system',
            name='boards',
            field=models.ManyToManyField(blank=True, default=None, help_text='Select one or multiple boards...', to='products.Board'),
        ),
        migrations.AlterField(
            model_name='system',
            name='certification',
            field=models.ManyToManyField(blank=True, default=None, help_text='Select one or multiple certifications...', to='products.Certification'),
        ),
        migrations.AlterField(
            model_name='system',
            name='configuration',
            field=models.ManyToManyField(blank=True, default=None, help_text='Select one or multiple configurations...', to='products.Configuration'),
        ),
        migrations.AlterField(
            model_name='system',
            name='package',
            field=models.ManyToManyField(blank=True, default=None, help_text='Select one or multiple packages...', to='products.Package'),
        ),
        migrations.AlterField(
            model_name='system',
            name='vendor',
            field=models.ManyToManyField(blank=True, default=None, help_text='Select one or multiple vendor locations', to='products.MfgLoc', verbose_name='Vendor Locations'),
        ),
    ]
