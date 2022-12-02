from django.db import models
import uuid
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
# Create your models here.


class Status(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    status = models.CharField(max_length=20)
    status_order = models.PositiveSmallIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Status'

    def __str__(self):
        return self.status


class Team(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    team_name = models.CharField(max_length=200)

    def __str__(self):
        return self.team_name


class Project(models.Model):

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    project_code = models.CharField(max_length=40, validators=[
        MinLengthValidator(6)], default="MISSING")
    team = models.ForeignKey(
        Team, null=True, blank=False,  on_delete=models.PROTECT, related_name='projects')
    title = models.CharField(max_length=200, validators=[
        MinLengthValidator(3)])
    description = models.TextField(null=True, validators=[
        MinLengthValidator(3)])
    featured_image = models.ImageField(
        null=True, blank=True, default="default.jpg", upload_to='images/projects/')
    status = models.ForeignKey(
        Status, null=True, blank=False,  on_delete=models.PROTECT, related_name='projects')

    def __str__(self):
        return self.title


class Run(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    run_name = models.CharField(max_length=100, default="RUN_NAME", validators=[
        MinLengthValidator(3)])
    project_id = models.PositiveIntegerField(
        default=0, verbose_name="analyst")
    analyst_id = models.PositiveIntegerField(
        default=0, verbose_name="analyst")
    purpose = models.CharField(max_length=300, validators=[
        MinLengthValidator(3)])
    conclusion = models.TextField(null=True, validators=[
        MinLengthValidator(3)])
    notebook_name = models.CharField(max_length=100, validators=[
        MinLengthValidator(3)])
    notebook_location = models.CharField(
        max_length=400,  default='LIBRARY', validators=[MinLengthValidator(3)])
    notebook_file = models.FileField(null=True, blank=True, upload_to='data/')
    results = models.TextField(null=True, validators=[
        MinLengthValidator(3)])
    comments = models.TextField(null=True, validators=[
        MinLengthValidator(3)])

    def __str__(self):
        return self.run_name


class Metric(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, default="RUN_NAME", validators=[
        MinLengthValidator(3)])

    def __str__(self):
        return f"METRIC: {self.name}"


class RunMetrics(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    run_id = models.ForeignKey(Run,  on_delete=models.PROTECT)
    metric_id = models.ForeignKey(Metric, on_delete=models.PROTECT)
    value = models.FloatField()

    def __str__(self):
        return f"RUN-{self.run_id}-METRIC-{self.metric_id}"
