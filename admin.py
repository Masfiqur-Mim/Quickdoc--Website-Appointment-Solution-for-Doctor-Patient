# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import review,comment,reply_on_comment
# Register your models here.
admin.site.register(review)
admin.site.register(comment)
admin.site.register(reply_on_comment)