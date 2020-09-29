from django.contrib import admin
from .models import Event

# Register your models here.

class EventAdmin(admin.ModelAdmin):
	
    list_display = ('user', 'subject', 'description', 'start_time', 'end_time', 'clock', 'status')
    list_filter = ('user', 'subject', 'status')
    
    
    fieldsets = (
        (None, {'fields': ('user', 'subject', 'description')}),
        ('Event info', {'fields': ('start_time', 'end_time', 'clock', 'status',)}),
    )


    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user', 'subject', 'description', 'start_time', 'end_time', 'clock', 'status'),
        }),
    )
    
    search_fields = ('user', 'subject', 'description')
    ordering = ('user', 'subject',)
    filter_horizontal = ()

admin.site.register(Event, EventAdmin)