import uuid
from django.db import models


class Workspace(models.Model):
    """Container for projects, to be used in the future to partition projects by owner"""
    id = models.IntegerField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name


class Budget(models.Model):
    """Time and Meterial"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    time = models.DurationField(null=True)
    cost = models.DecimalField(max_digits=18,decimal_places=4,null=True)


class Project(models.Model):
    """Self contained project"""
    id = models.IntegerField(primary_key=True, editable=False)
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField()
    baseline = models.DateTimeField(null=True, blank=True)
    workspace = models.ForeignKey('Workspace')
    budget = models.ForeignKey('Budget', null=True, blank=True)
    def __str__(self):
        return self.name


class Task(models.Model):
    """Task"""
    id = models.AutoField(primary_key=True)
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    project = models.ForeignKey('Project')
    parent = models.ForeignKey('self',blank=True, null=True)
    budget = models.ForeignKey('Budget', null=True, blank=True)
    prerequisites = models.ManyToManyField('self',null=True, blank=True)
    def __str__(self):
        return self.name 
