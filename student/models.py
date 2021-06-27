from django.db.models import Model, CharField, DateField, EmailField, SmallIntegerField
from student.enums import Sex


# Create your models here.
class Student(Model):
    first_name = CharField(max_length=64, null=False, blank=False)
    last_name = CharField(max_length=64, null=False, blank=False)
    date_of_birth = DateField(null=False, blank=False)
    email = EmailField(max_length=128, null=False, blank=False)
    sex = SmallIntegerField(
        choices=((Sex.male.value, Sex.male.name), (Sex.female.value, Sex.female.name)),
        null=False,
        blank=False
    )

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.fullname} ({self.id})'


