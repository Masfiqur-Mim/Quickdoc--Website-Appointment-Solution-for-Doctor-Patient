# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import location,Doctor_has_sitting_on_location,appointment

# Register your models here.
admin.site.register(location)
admin.site.register(Doctor_has_sitting_on_location)
admin.site.register(appointment)