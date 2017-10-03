from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import *
# Create your views here.
def default(request):
    # return render(request,'',
    return HttpResponse('Test Page')

def workspace_detail(request, pk):
    workspace = get_object_or_404(Workspace, pk=pk) 
    return render(request, 'py_proj_man/workspace_detail.html', {'workspace':workspace})

def project_detail(request, ws_pk, proj_pk):
    project = get_object_or_404(Project, workspace = ws_pk, pk = proj_pk)
    return render(request, 'py_proj_man/project_detail.html', {'project':project})

def task_detail(request, ws_pk, proj_pk, task_pk):
    task = get_object_or_404(Task,  project = proj_pk, pk=task_pk)
    return render(request, 'py_proj_man/task_detail.html', {'task':task})
