from django.contrib import admin
from .models import CustomUser, WorkArea

class WorkAreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(CustomUser)
admin.site.register(WorkArea)
