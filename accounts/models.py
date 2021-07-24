from django.contrib.auth.models import User
from django.db.models import Model, OneToOneField, CASCADE, TextField, ForeignKey, PROTECT, CharField

from student.models import Address


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    biography = TextField()
    personal_phone = CharField(max_length=32, default='', null=False, blank=False)
    permanent_address = ForeignKey(Address, on_delete=PROTECT, null=True)
