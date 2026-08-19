from django.contrib import admin
from .models import TaskList

# Register your models here.
#@admin.register(TaskList)
#class TaskListAdmin(admin.ModelAdmin):
    #list_display = ('id','task','done')
    #search_fields = ('task',)
    #list_filter = ('task',)

admin.site.register(TaskList)
