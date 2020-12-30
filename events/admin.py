from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'location',
        'date_and_time',
        'description',
        'timestamp',
    )


admin.site.register(Event, EventAdmin)
