from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import RSVP
@admin.register(RSVP)
class RSVPAdmin(admin.ModelAdmin):
    list_display = ('name', 'attendance', 'created_at')
    list_filter = ('attendance', 'created_at')
    search_fields = ('name',)
