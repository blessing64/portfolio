from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.decorators import login_required
from . models import Project

# Create your views here.
def projects(request):
    my_project = Project.objects.all()
    return render(request, "project/project.html", {"my_project" : my_project})


def add_project(request):
    if request.method == "POST":
        form = forms.ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    else:
        form = forms.ProjectForm()
    return render(request,"project/add.html", {'form':form})  

@login_required(login_url="login")
def detail_project(request, pk):
    singleproject = Project.objects.get(pk = pk) 
    return render(request, "project/project_details.html", {"singleproject" : singleproject})


def delete_project(request, pk):
    oneProject = Project.objects.get(pk = pk)
    if request.method == "POST":
        oneProject.delete()
        return redirect("projects")
        