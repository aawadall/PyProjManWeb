"""PyProjMan Views"""
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Project, Task, Workspace

def default(request):
    """Default view, to fallback to whenever there is nothing to show"""
    # return render(request,'',
    return HttpResponse('Test Page')

def workspace_detail(request, pk):
    """Workspace View, Takes pk as an argument to lookup workspace"""
    workspace = get_object_or_404(Workspace, pk=pk)
    return render(request, 'py_proj_man/workspace_detail.html', {'workspace':workspace})

def project_detail(request, ws_pk, proj_pk):
    """Project Detailed View, takes ws_pk and proj_pk as arguments to lookup a workspace/project pair"""
    project = get_object_or_404(Project, workspace = ws_pk, pk = proj_pk)
    return render(request, 'py_proj_man/project_detail.html', {'project':project})

def task_detail(request, ws_pk, proj_pk, task_pk):
    """Task Detailed View, takes ws_pk, proj_pk and task_pk as arguments to lookup workspace/project/task tuple"""
    task = get_object_or_404(Task,  project = proj_pk, pk=task_pk)
    return render(request, 'py_proj_man/task_detail.html', {'task':task})

