from django.db import models


class A(models.Model):
    bigtext = models.TextField()
    name = models.CharField(max_length=100)
    counter = models.IntegerField(default=0)


class B(models.Model):
    parent = models.ForeignKey(A, related_name="bs")
    bigtext = models.TextField()
    counter = models.IntegerField(default=0)


class C(models.Model):
    parent = models.ForeignKey(B, related_name="cs")
    grandparent = models.ForeignKey(A, related_name="cs")
    bigtext = models.TextField()
    counter = models.IntegerField(default=0)


