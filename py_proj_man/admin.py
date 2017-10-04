from django.contrib import admin
from .models import Workspace, Project, Budget, Task
"""PyProjMan Administration Module"""


class TaskInline(admin.StackedInline):
    """Tasks defined inline with Projects"""
    model = Task


class ProjectAdmin(admin.ModelAdmin):
    """Project Administraion"""
    inlines = [TaskInline,]


class ProjectInline(admin.StackedInline):
    """Projects defined inline in a workspace"""
    model = Project


class WorkspaceAdmin(admin.ModelAdmin):
    """Worjkspace administration"""
    inlines = [ProjectInline,]
 
admin.site.register(Workspace, WorkspaceAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Budget)
admin.site.register(Task)

