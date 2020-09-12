from django.contrib import admin
from .models import Event

# Register your models here.

class EventAdmin(admin.ModelAdmin):
	
    list_display = ('subject', 'description', 'start_time', 'clock', 'status')
    list_filter = ('subject', 'status')
    
    
    fieldsets = (
        (None, {'fields': ('subject', 'description')}),
        ('Event info', {'fields': ('start_time', 'clock', 'status',)}),
    )


    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('subject', 'description', 'start_time', 'clock', 'status'),
        }),
    )
    
    search_fields = ('subject', 'description')
    ordering = ('subject',)
    filter_horizontal = ()

admin.site.register(Event, EventAdmin)