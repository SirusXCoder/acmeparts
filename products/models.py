
from django.db import models

import json

from django.core import serializers


class PackageManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)


class Package(models.Model):
    objects = PackageManager()
    name = models.CharField(
        max_length=32,
        help_text='Enter Package',
        unique=True,
    )

    # def natural_key(self):
    #     return (self.name)

    class Meta:
        verbose_name = 'Package'

    def __str__(self):
        return self.name


class CertManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)


class Certification(models.Model):
    objects = CertManager()
    name = models.CharField(
        max_length=20,
        help_text='Enter Certification',
    )

    class Meta:
        verbose_name = 'Certification'

    def __str__(self):
        return self.name


class FormManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)


class FormFactor(models.Model):
    objects = FormManager()
    name = models.CharField(
        max_length=32,
        verbose_name='Form Factor',
        help_text='Enter Form Factor',
    )

    class Meta:
        verbose_name = 'Form Factor'

    def __str__(self):
        return self.name


class MfgLocManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)


class MfgLoc(models.Model):
    objects = MfgLocManager()
    name = models.CharField(
        max_length=50,
        verbose_name='Name',
        help_text='Enter Location Name',
    )

    address = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        verbose_name='Address',
        help_text='Enter Address',
    )

    address2 = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        verbose_name='2nd Address',
        help_text='Enter Address',
    )

    city = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        verbose_name='City',
        help_text='Enter City',
    )

    state = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        verbose_name='State',
        help_text='Enter State',
    )

    country = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        verbose_name='Country',
        help_text='Enter country',
    )

    class Meta:
        verbose_name = 'Vendor Location'

    def __str__(self):
        return self.name


class ConfigurationManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)


class Configuration(models.Model):
    objects = ConfigurationManager()
    name = models.CharField(
        max_length=50,
    )

    class Meta:
        verbose_name = 'Configuration'

    def __str__(self):
        return self.name


class BoardManager(models.Manager):
    def get_by_natural_key(self, pn):
        return self.get(pn=pn)


class Board(models.Model):
    objects = BoardManager()
    pn = models.CharField(
        max_length=32,
        verbose_name='Product #:',
        help_text='Enter product number',
    )

    sn = models.CharField(
        max_length=32,
        verbose_name='Serial #:',
        help_text='Enter serial number',
    )

    # chips = models.ForeignKey(
    #     "Chip",
    #     blank=True,
    #     null=True,
    #     default=None,
    #     related_name='bdchips',
    #     help_text='Select one or multiple chips...',
    #     on_delete=models.SET_NULL,
    # )

    chips = models.ManyToManyField(
        "Chip",
        blank=True,
        # null=True,
        # default=None,
        # related_name='bdchips',
        help_text='Select one or multiple chips...',
    )

    description = models.TextField(
        null=True,
        blank=True,
        help_text='Description text...',
    )

    certification = models.ManyToManyField(
        Certification,
        blank=True,
        # null=True,
        default=None,
        help_text='Select one or multiple certifications',
    )

    assigned_to = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        verbose_name='Assigned To',
        help_text='Input assign to',
    )

    mfg_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Manufacture Date',
        help_text='Select or input a date',
    )

    vendor = models.ManyToManyField(
        MfgLoc,
        blank=True,
        # null=True,
        verbose_name='Vendor Locations',
        help_text='Select one or multiple vendor locations',
    )

    mac_address = models.CharField(
        max_length=17,
        null=True,
        blank=True,
        verbose_name='MAC Address',
        help_text='Enter MAC Address',
    )

    service_log = models.TextField(
        null=True,
        blank=True,
        verbose_name='Service Log',
        help_text='Enter service log details',
    )

    class Meta:
        verbose_name = 'Board'

    def __str__(self):
        return f'{self.pn} ({self.sn})'


class SystemManager(models.Manager):
    def get_by_natural_key(self, pn):
        return self.get(pn=pn)


class System(models.Model):

    objects = SystemManager()

    pn = models.CharField(
        max_length=32,
        verbose_name='Product #:',
        help_text='Enter product number',
    )

    sn = models.CharField(
        max_length=32,
        verbose_name='Serial #:',
        help_text='Enter serial number',
    )

    boards = models.ManyToManyField(
        Board,
        blank=True,
        default=None,
        help_text='Select one or multiple boards...',
    )

    description = models.TextField(
        null=True,
        blank=True,
        help_text='Description text...',
    )

    package = models.ManyToManyField(
        Package,
        blank=True,
        default=None,
        help_text='Select one or multiple packages...',
    )

    certification = models.ManyToManyField(
        Certification,
        blank=True,
        default=None,
        help_text='Select one or multiple certifications...',
    )

    assigned_to = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        verbose_name='Assigned To',
        help_text='Input assign to',
    )

    formfactor = models.ForeignKey(
        FormFactor,
        on_delete=models.DO_NOTHING,
        default=None,
        null=True,
        blank=True,
        verbose_name='Form Factor',
        help_text='Select a form factor',
    )

    mfg_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Manufacture Date',
        help_text='Select or input a date'
    )

    vendor = models.ManyToManyField(
        MfgLoc,
        blank=True,
        default=None,
        verbose_name='Vendor Locations',
        help_text='Select one or multiple vendor locations',
    )

    mac_address = models.CharField(
        max_length=17,
        blank=True,
        verbose_name='MAC Address',
        help_text='Enter MAC Address',
    )

    configuration = models.ManyToManyField(
        Configuration,
        blank=True,
        default=None,
        help_text='Select one or multiple configurations...',
    )

    service_log = models.TextField(
        null=True,
        blank=True,
        verbose_name='Service Log',
        help_text='Enter service log details',
    )

    class Meta:
        verbose_name = 'System'

    def __str__(self):
        return f'{self.pn} ({self.sn})'
        pass


class ChipManager(models.Manager):
    def get_by_natural_key(self, pn):
        return self.get(pn=pn)


class Chip(models.Model):
    pn = models.CharField(
        max_length=32,
        verbose_name='Product #:',
        help_text='Enter product number',
    )

    sn = models.CharField(
        max_length=32,
        verbose_name='Serial #:',
        help_text='Enter serial number',
    )

    description = models.TextField(
        null=True,
        blank=True,
        help_text='Description text...',
    )

    package = models.ManyToManyField(
        Package,
        blank=True,
        default=None,
        help_text='Select one or multiple packages...',
    )

    mfg_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Manufacture Date',
        help_text='Select or input a date',
    )

    vendor = models.ManyToManyField(
        MfgLoc,
        blank=True,
        default=None,
        verbose_name='Vendor Locations',
        help_text='Select one or multiple vendor locations',
    )

    speed_grade = models.IntegerField(
        default=0,
        null=True,
        blank=True,
        verbose_name='Speed Grade',
        help_text='Set speed grade',
    )

    objects = ChipManager()

    class Meta:
        verbose_name = 'Chip'

    def __str__(self):
        return f'{self.pn} ({self.sn})'
