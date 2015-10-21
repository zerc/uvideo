# coding: utf-8
from django.contrib import admin

from . import models


class VideoInline(admin.StackedInline):
    model = models.Video


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    inlines = (VideoInline,)
