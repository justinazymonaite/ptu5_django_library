from django.contrib import admin
from . import models


class BookInstanceInline(admin.TabularInline):
    model = models.BookInstance
    extra = 0
    readonly_fields = ('unique_id', )
    can_delete = False


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = (BookInstanceInline, ) # butinai reikia kablelio, kad butu kaip tuple


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('unique_id', 'book', 'status', 'due_back')
    list_filter = ('status', 'due_back')
    readonly_fields = ('unique_id', ) # butinai reikia kablelio, kad butu kaip tuple

    fieldsets = (
        ('General', {'fields': ('unique_id', 'book')}),
        ('Availability', {'fields': (('status', 'due_back'),)}), # idejus tuple i tuple galime padaryti, kad laukai atsidurtu vienoje eiluteje
    )


admin.site.register(models.Author)
admin.site.register(models.Genre)
admin.site.register(models.Book, BookAdmin)
admin.site.register(models.BookInstance, BookInstanceAdmin)