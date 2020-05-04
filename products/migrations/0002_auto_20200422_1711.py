# Generated by Django 3.0.5 on 2020-04-22 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formfactor',
            options={'verbose_name': 'Form Factor'},
        ),
        migrations.AlterModelOptions(
            name='mfgloc',
            options={'verbose_name': 'Vendor Location'},
        ),
        migrations.AlterField(
            model_name='board',
            name='certification',
            field=models.ManyToManyField(blank=True, default=None, help_text='Select one or multiple certifications', null=True, to='products.Certification'),
        ),
        migrations.AlterField(
            model_name='board',
            name='chips',
            field=models.ManyToManyField(blank=True, help_text='Select one or multiple chips...', null=True, to='products.Chip'),
        ),
        migrations.AlterField(
            model_name='board',
            name='vendor',
            field=models.ManyToManyField(blank=True, help_text='Select one or multiple vendor locations', null=True, to='products.MfgLoc', verbose_name='Vendor Locations'),
        ),
        migrations.AlterField(
            model_name='chip',
            name='package',
            field=models.ManyToManyField(blank=True, default=None, help_text='Select one or multiple packages...', null=True, to='products.Package'),
        ),
        migrations.AlterField(
            model_name='chip',
            name='vendor',
            field=models.ManyToManyField(blank=True, default=None, help_text='Select one or multiple vendor locations', null=True, to='products.MfgLoc', verbose_name='Vendor Locations'),
        ),
        migrations.AlterField(
            model_name='mfgloc',
            name='name',
            field=models.CharField(help_text='Enter Location Name', max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='package',
            name='name',
            field=models.CharField(help_text='Enter Package', max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='system',
            name='boards',
            field=models.ManyToManyField(blank=True, default=None, help_text='Select one or multiple boards...', null=True, to='products.Board'),
        ),
        migrations.AlterField(
            model_name='system',
            name='certification',
            field=models.ManyToManyField(blank=True, default=None, help_text='Select one or multiple certifications...', null=True, to='products.Certification'),
        ),
        migrations.AlterField(
            model_name='system',
            name='configuration',
            field=models.ManyToManyField(blank=True, default=None, help_text='Select one or multiple configurations...', null=True, to='products.Configuration'),
        ),
        migrations.AlterField(
            model_name='system',
            name='formfactor',
            field=models.ForeignKey(blank=True, default=None, help_text='Select a form factor', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='products.FormFactor', verbose_name='Form Factor'),
        ),
        migrations.AlterField(
            model_name='system',
            name='package',
            field=models.ManyToManyField(blank=True, default=None, help_text='Select one or multiple packages...', null=True, to='products.Package'),
        ),
        migrations.AlterField(
            model_name='system',
            name='vendor',
            field=models.ManyToManyField(blank=True, default=None, help_text='Select one or multiple vendor locations', null=True, to='products.MfgLoc', verbose_name='Vendor Locations'),
        ),
    ]