from datetime import date

from django.core.exceptions import ValidationError
from django.forms import Form, CharField, ChoiceField, EmailField, DateField, ModelChoiceField, ModelForm
from student.choices import SEX_TYPES
from student.models import Employment, Student, Employer, Address, Contact


def first_name_many_words(value: str):
    if len(value.split()) > 1:
        raise ValidationError('First name must contain only one word.')


def proper_phone_number(value: str):
    if value[0] != '+':
        raise ValidationError('Enter the valid number with the prefix')


def is_number(value: str):
    if not value.isdigit():
        raise ValidationError('Enter number')


class RealDateOfBirthField(DateField):
    def validate(self, value: date):
        super().validate(value)
        if (date.today() - value).days > 90 * 365:
            raise ValidationError('Student is too old. More than 90 years old.')


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    first_name = CharField(min_length=2, max_length=64, required=True, validators=[first_name_many_words])
    last_name = CharField(min_length=2, max_length=64, required=True)
    date_of_birth = RealDateOfBirthField(required=True)
    sex = ChoiceField(choices=SEX_TYPES, required=True)
    email = EmailField(max_length=128, required=True)
    employment = ModelChoiceField(queryset=Employment.objects, required=False)
    permanent_address = ModelChoiceField(queryset=Address.objects, required=False)

    def clean_first_name(self):
        return self.cleaned_data['first_name'].lower().capitalize()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].lower().capitalize()

    def clean_email(self):
        return self.cleaned_data['email'].lower()


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    work_phone = CharField(min_length=13, max_length=16, required=True, validators=[proper_phone_number])
    personal_phone = CharField(min_length=13, max_length=16, required=False, validators=[proper_phone_number])
    email = EmailField(max_length=128, required=False)
    student = ModelChoiceField(queryset=Student.objects, required=False)

    def clean_email(self):
        return self.cleaned_data['email'].lower()

    def clean_work_phone(self):
        raw_result = self.cleaned_data['work_phone']
        result = raw_result[:4] + ' ' + raw_result[4:7] + ' ' + raw_result[7:10] + ' ' + raw_result[10:]
        return result

    def clean_personal_phone(self):
        raw_result = self.cleaned_data['personal_phone']
        result = raw_result[:4] + ' ' + raw_result[4:7] + ' ' + raw_result[7:10] + ' ' + raw_result[10:]
        return result

    def clean(self):
        result = super().clean()

        if not self.is_valid():
            return result

        if (
                not self.cleaned_data['work_phone'] and
                not self.cleaned_data['personal_phone'] and
                not self.cleaned_data['email']
        ):
            raise ValidationError('At least one contact must be filled')

        exists_flag = Contact.objects.filter(
            student=self.cleaned_data['student'],
            work_phone=self.cleaned_data['work_phone'],
            personal_phone=self.cleaned_data['personal_phone'],
            email=self.cleaned_data['email']
        ).exists()

        if exists_flag:
            raise ValidationError('This contact already exists')

        return result


class AddressForm(Form):
    street = CharField(min_length=3, max_length=128, required=True)
    house_number = CharField(max_length=16, required=True, validators=[is_number])
    city = CharField(max_length=64, required=True)
    zip_code = CharField(min_length=5, max_length=16, required=True, validators=[is_number], label='ZIP code')
    country_iso3 = CharField(min_length=3, max_length=3, required=True, label='Country ISO-3')

    def clean_street(self):
        return self.cleaned_data['street'].lower().capitalize()

    def clean_country_iso3(self):
        return self.cleaned_data['country_iso3'].upper()


class EmployerForm(ModelForm):
    class Meta:
        model = Employer
        fields = '__all__'  # nebo tuple ('name', 'address')

    name = CharField(max_length=64, required=True)
    address = ModelChoiceField(queryset=Address.objects, required=True)
