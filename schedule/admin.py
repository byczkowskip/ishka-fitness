from django.contrib import admin

from schedule.models import Session


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'date', 'start_time', 'end_time', 'duration', 'max_clients']
    search_fields = ['date', 'start_time', 'end_time']
    list_filter = ['title', 'date', 'start_time', 'end_time']
