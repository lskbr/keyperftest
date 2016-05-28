from django.db import models
import uuid

# Create your models here.


class A(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bigtext = models.TextField()
    name = models.CharField(max_length=100)
    counter = models.IntegerField(default=0)


class B(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parent = models.ForeignKey(A, related_name="bs")
    bigtext = models.TextField()
    counter = models.IntegerField(default=0)


class C(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parent = models.ForeignKey(B, related_name="cs")
    grandparent = models.ForeignKey(A, related_name="cs")
    bigtext = models.TextField()
    counter = models.IntegerField(default=0)
