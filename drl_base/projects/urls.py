from django.urls import path

from . import views_projects, views_runs
app_name = 'projects'
urlpatterns = [
    path('', views_projects.projects, name="projects"),
    path('project/<str:pk>/', views_projects.project, name="project"),
    path('create-project/', views_projects.createProject, name="create-project"),
    path('update-project/<str:pk>/',
         views_projects.updateProject, name="update-project"),
    path('project-delete/<str:pk>/',
         views_projects.deleteProject, name="project-delete"),
    path('project-delete-confirm/<str:pk>/',
         views_projects.deleteProjectConfirm, name="project-delete-confirm"),
    path('runs/', views_runs.runs, name="runs"),
    path('create-run/', views_runs.createRunCSV, name="create-run-csv"),
    path('run/<str:pk>/', views_runs.run, name="run"),
]
