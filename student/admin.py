from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin, TabularInline

from student.models import Employer, Address, Student, Employment, Contact, MediaData, SocialMedia


class EmployerAdmin(ModelAdmin):
    pass


class AddressAdmin(ModelAdmin):
    pass


class EmploymentAdmin(ModelAdmin):
    pass


class ContactAdmin(ModelAdmin):
    pass


class MediaDataAdmin(ModelAdmin):
    pass


class SocialMediaAdmin(ModelAdmin):
    pass


class ContactInline(TabularInline):
    model = Contact


class MediaDataInline(TabularInline):
    model = MediaData


class SocialMediaInline(TabularInline):
    model = SocialMedia


class StudentAdmin(ModelAdmin):
    fieldsets = [
        (
            'Personal Information',
            {
             'fields': ['email', 'first_name', 'last_name', 'date_of_birth', 'sex', 'permanent_address']
            }
         ),
        (
            'Employment',
            {
                'fields': ['employment']
            }
        ),
    ]

    inlines = [ContactInline, MediaDataInline, SocialMediaInline]


admin.site.register(Employer, EmployerAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Employment, EmploymentAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(MediaData, MediaDataAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
