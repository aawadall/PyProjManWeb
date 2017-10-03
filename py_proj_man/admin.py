from django.contrib import admin
from .models import Workspace, Project, Budget, Task
# Register your models here.

class TaskInline(admin.StackedInline):
    model = Task 

class ProjectAdmin(admin.ModelAdmin):
    inlines = [TaskInline,]

class ProjectInline(admin.StackedInline):
    model = Project 

class WorkspaceAdmin(admin.ModelAdmin):
    inlines = [ProjectInline,]
 
admin.site.register(Workspace, WorkspaceAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Budget)
admin.site.register(Task)
