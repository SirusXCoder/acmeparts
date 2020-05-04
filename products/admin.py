from django.contrib import admin

# Register your models here

admin.site.site_header = 'ACME Admin'
admin.site.site_title = 'ACME Admin Area'
admin.site.site_index = 'Welcome to the ACME Admin Area'

from.models import Package, Certification, FormFactor, MfgLoc, Configuration,  Board, Chip, System

admin.site.register(Package)
admin.site.register(Certification)
admin.site.register(FormFactor)
admin.site.register(MfgLoc)
admin.site.register(Configuration)
admin.site.register(Board)
admin.site.register(System)
admin.site.register(Chip)
