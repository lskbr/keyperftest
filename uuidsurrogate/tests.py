from django.test import TestCase
from ptest.util import timed
from django.db.models import F
from faker import Factory
from uuidsurrogate.models import *
from django.conf import settings
import random
# Create your tests here.


class UUIDTest(TestCase):
    @timed
    def uuidsurrogate_insert_many(self):
        fake = Factory.create()
        for _ in range(settings.N):
            a = A.objects.create(bigtext=fake.text(), name=fake.name())
            b = B.objects.create(bigtext=fake.text(), parent=a)
            C.objects.create(bigtext=fake.text(), parent=b, grandparent=a)

    @timed
    def uuidsurrogate_update_many(self):
        for c in C.objects.all():
            c.parent.counter = F('counter') + 1
            c.grandparent.counter = F('counter') + 1
            c.parent.save()
            c.grandparent.save()
            c.save()

    @timed
    def uuidsurrogate_random_get(self):
        ids = [c.surrogate_id for c in C.objects.only('surrogate_id').all()]
        random.shuffle(ids)
        for c_sid in ids:
            C.objects.get(surrogate_id=c_sid)

    def test(self):
        self.uuidsurrogate_insert_many()
        self.uuidsurrogate_update_many()
        self.uuidsurrogate_random_get()



