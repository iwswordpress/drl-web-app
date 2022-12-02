
from django.shortcuts import render, redirect

from .forms import ProjectForm
from .models import Project


def projects(request):
    # projects, search_query = searchProjects(request)
    # custom_range, projects = paginateProjects(request, projects, 6)
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project = Project.objects.get(id=pk)
    context = {'project': project}
    return render(request, 'projects/project-detail.html', context)


def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():

            project = form.save(commit=False)
            uploaded_image = request.FILES.get("featured_image")
            if uploaded_image:
                print('created ', uploaded_image)
                project.featured_image = uploaded_image
            project.save()

            return redirect('projects:projects')

    context = {'form': form}
    return render(request, "projects/project-form.html", context)


def updateProject(request, pk):

    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    print('UPDATE')
    if request.method == 'POST':
        print('POST')
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save(commit=False)
            uploaded_image = request.FILES.get("featured_image")
            if uploaded_image:
                print('uploaded ', uploaded_image)
                project.featured_image = uploaded_image
            project.save()

            return redirect('projects:projects')

    context = {'form': form, 'project': project}
    return render(request, "projects/project-update.html", context)


def deleteProjectConfirm(request, pk):
    print('pk', pk)
    project = Project.objects.get(id=pk)
    context = {'project': project}
    return render(request, 'projects/project-delete-confirm.html', context)


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'GET':
        project.delete()
        return redirect('projects:projects')
    context = {'project': project}
    return render(request, 'projects/delete-project.html', context)
