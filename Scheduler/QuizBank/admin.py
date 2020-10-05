from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Quiz
# Register your models here.

@admin.register(Quiz)
class QuixAdmin(ImportExportModelAdmin):
    list_display = ('id', 'subject', 'year', 'question1', 'question2', 'question3', 'answer')
    list_filter = ('subject', 'year')

    
    search_fields = ('subject', 'year', 'question1')
    ordering = ('subject', 'year')
    filter_horizontal = ()