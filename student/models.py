from django.db.models import Model, CharField, DateField, EmailField, SmallIntegerField, PROTECT, \
     URLField, ForeignKey, CASCADE, Count, FileField
from student.enums import Sex, FileType
from student.utils.storage import upload_to_student_dir


# Create your models here.
class Address(Model):
    street = CharField(max_length=128, null=False, blank=False)
    house_number = CharField(max_length=16, null=False, blank=False)
    zip_code = CharField(max_length=16, null=False, blank=False)
    country_iso3 = CharField(max_length=3, null=False, blank=False)


class Employer(Model):
    name = CharField(max_length=64, null=False, blank=False)
    address = ForeignKey('Address', null=False, on_delete=PROTECT)

    def __str__(self):
        return f"{self.name} ({self.id})"

    @property
    def employees_count(self):
        return self.employments.aggregate(employees_cnt=Count('employees'))['employees_cnt']


class Employment(Model):
    employer = ForeignKey('Employer', null=False, on_delete=PROTECT, related_name='employments')

    position = CharField(max_length=128, null=False, blank=False)

    def __str__(self):
        return f"{self.position} ({self.id})"


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

    permanent_address = ForeignKey('Address', on_delete=PROTECT, null=True)
    employment = ForeignKey('Employment', on_delete=PROTECT, null=True, related_name='employees')

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.fullname} ({self.id})'


class Contact(Model):
    class Meta:
        unique_together = (
            'student',
            'work_phone',
            'personal_phone',
            'email'
        )

    student = ForeignKey('Student', null=False, on_delete=CASCADE, related_name='contacts')

    work_phone = CharField(max_length=32, default='', null=False, blank=True)
    personal_phone = CharField(max_length=32, default='', null=False, blank=False)
    email = EmailField(max_length=128, default='', null=False, blank=False)

    def __str__(self):
        return f'Student ID ({self.student_id}) ({self.id})'


class SocialMedia(Model):
    student = ForeignKey('Student', null=False, on_delete=CASCADE, related_name='social_medias')

    instagram = URLField(default='', null=False, blank=True)
    facebook = URLField(default='', null=False, blank=True)


class MediaData(Model):
    student = ForeignKey('Student', null=False, on_delete=CASCADE, related_name='media_files')

    file = FileField(max_length=512, null=False, upload_to=upload_to_student_dir)
    type = SmallIntegerField(
        choices=((FileType.photo.value, FileType.photo.name), (FileType.video.value, FileType.video.name)),
        null=False,
        blank=False
    )
