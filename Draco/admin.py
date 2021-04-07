from django.contrib import admin
from .models import *


@admin.register(Dragon)
class DragonAdmin(admin.ModelAdmin):
    list_display = ("id", "image_1", "image_2", "image_3", "usual_pic")
    list_display_links = ("id",)


@admin.register(PIC)
class PICAdmin(admin.ModelAdmin):
    list_display = ("id", "image_1", "image_2")
    list_display_links = ("id",)


@admin.register(PICweb)
class PICwebAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "text")
    list_display_links = ("id",)
