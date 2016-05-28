from django.db import models
import uuid


class A(models.Model):
    surrogate_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    bigtext = models.TextField()
    name = models.CharField(max_length=100)
    counter = models.IntegerField(default=0)


class B(models.Model):
    surrogate_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    parent = models.ForeignKey(A, related_name="bs")
    bigtext = models.TextField()
    counter = models.IntegerField(default=0)


class C(models.Model):
    surrogate_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    parent = models.ForeignKey(B, related_name="cs")
    grandparent = models.ForeignKey(A, related_name="cs")
    bigtext = models.TextField()
    counter = models.IntegerField(default=0)


