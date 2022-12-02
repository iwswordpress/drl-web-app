import csv
import pandas as pd
import os

from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.models import User


from .forms import RunForm
from .models import Run


def read_csv(file):
    data = []

    with open(file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            row = "".join(row)
            row = row.replace(";", " ")
            print('row is', row)
            data.append(row)
    print('data--->', data)
    return data


def runs(request):
    # projects, search_query = searchProjects(request)
    # custom_range, projects = paginateProjects(request, projects, 6)
    runs = Run.objects.all()
    context = {'runs': runs}
    return render(request, 'projects/runs/runs.html', context)


def createRunCSV(request):
    form = RunForm()

    if request.method == 'POST':
        form = RunForm(request.POST, request.FILES)

        if form.is_valid():
            run = form.save(commit=False)
            uploaded_file = request.FILES.get("notebook_file")
            if uploaded_file:

                uploads_location = settings.MEDIA_ROOT
                print('location', uploads_location)
                csv_filename = str(uploads_location) + \
                    '\\data\\' + str(uploaded_file)
                print('csv_filename', csv_filename)

                run.notebook_file = uploaded_file
                run.analyst_id = 1
            run.save()
            uploaded_data = read_csv(csv_filename)
            # report_data
            # We will need to add a new hyperparameter 1
            # Works OK 2
            # my first run 3
            # GITHUB-REPO01 4
            # 01-test.ipynb 5
            # 1 6
            # Purpose:Test data 7
            # "{'mae': 2.0, 'rmse': 3.5, 'auc': 2.1}" 8
            run.comments = uploaded_data[1]
            run.conclusion = uploaded_data[2]
            run.run_name = uploaded_data[3]
            run.notebook_location = uploaded_data[4]
            run.notebook_name = uploaded_data[5]
            run.project_id = uploaded_data[6]
            run.purpose = uploaded_data[7]
            run.results = uploaded_data[8]
            run.save()

            # if os.path.exists(csv_filename):
            #     os.remove(csv_filename)
            # else:
            #     print("The file does not exist")
            return redirect('projects:runs')

    context = {'form': form}
    return render(request, "projects/runs/run-form.html", context)


def run(request, pk):
    run = Run.objects.get(id=pk)
    context = {'run': run}
    return render(request, 'projects/runs/run-detail.html', context)


# def updateProject(request, pk):

#     project = Project.objects.get(id=pk)
#     form = ProjectForm(instance=project)
#     print('UPDATE')
#     if request.method == 'POST':
#         print('POST')
#         form = ProjectForm(request.POST, request.FILES, instance=project)
#         if form.is_valid():
#             project = form.save(commit=False)
#             uploaded_image = request.FILES.get("featured_image")
#             if uploaded_image:
#                 print('uploaded ', uploaded_image)
#                 project.featured_image = uploaded_image
#             project.save()

#             return redirect('projects:projects')

#     context = {'form': form, 'project': project}
#     return render(request, "projects/update-project.html", context)


# def deleteProjectConfirm(request, pk):
#     print('pk', pk)
#     project = Project.objects.get(id=pk)
#     context = {'project': project}
#     return render(request, 'projects/delete-project-confirm.html', context)


# def deleteProject(request, pk):
#     project = Project.objects.get(id=pk)
#     if request.method == 'GET':
#         project.delete()
#         return redirect('projects:projects')
#     context = {'project': project}
#     return render(request, 'projects/delete-project.html', context)
