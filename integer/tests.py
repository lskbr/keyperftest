from django.test import TestCase
from ptest.util import timed
from django.db.models import F
from faker import Factory
from integer.models import *
from django.conf import settings
import random
# Create your tests here.



class IntegerTest(TestCase):

    @timed
    def insert_many(self):
        fake = Factory.create()
        for _ in range(settings.N):
            a = A.objects.create(bigtext=fake.text(), name=fake.name())
            b = B.objects.create(bigtext=fake.text(), parent=a)
            c = C.objects.create(bigtext=fake.text(), parent=b, grandparent=a)


    @timed
    def update_many(self):
        for c in C.objects.all():
            c.parent.counter = F('counter') + 1
            c.grandparent.counter = F('counter') + 1
            c.parent.save()
            c.grandparent.save()
            c.save()

    @timed
    def random_get(self):
        ids = [c.id for c in C.objects.only('id').all()]
        random.shuffle(ids)
        for c_sid in ids:
            C.objects.get(id=c_sid)

    def test(self):
        self.insert_many()
        self.update_many()
        self.random_get()
