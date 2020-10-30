from django.contrib import admin
from .models import Link ,TestType
# Register your models here.

class GradeAdmin(admin.ModelAdmin):
	
    list_display = ('user', 'date', 'subject', 'test', 'scope', 'grade')
    list_filter = ('user', 'subject')
    
    
    fieldsets = (
        (None, {'fields': ('user', 'subject',)}),
        ('Event info', {'fields': ('date', 'test', 'scope', 'grade',)}),
    )


    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user', 'date', 'subject', 'test', 'scope', 'grade'),
        }),
    )
    
    search_fields = ('user', 'subject',)
    ordering = ('user', 'subject',)
    filter_horizontal = ()

admin.site.register(Link, GradeAdmin)
admin.site.register(TestType)


# Register your models here.

