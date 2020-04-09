from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ('user', 'verb', 'target', 'created')
    list_filter = ('created',)
    search_fields = ('verb',)
