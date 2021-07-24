from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db.transaction import atomic
from django.forms import CharField, Textarea, ModelChoiceField

from accounts.models import Profile
from student.models import Address


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

    biography = CharField(label='Tell us about you', widget=Textarea, min_length=42)
    personal_phone = CharField(max_length=32, required=False)

    # Transaction
    @atomic
    def save(self, commit=True):
        # self.instance.is_active = False
        result = super().save(commit)
        profile = Profile(
            user=result,
            personal_phone=self.cleaned_data['personal_phone'],
            biography=self.cleaned_data['biography']
        )

        if commit:
            profile.save()

        return result


class MeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = ['first_name', 'last_name', 'email']

    personal_phone = CharField(max_length=32, required=False)
    permanent_address = ModelChoiceField(queryset=Address.objects, required=False)

    @atomic
    def save(self, commit=True):
        # self.instance.is_active = False
        result = super().save(commit)
        result.profile.personal_phone = self.cleaned_data['personal_phone']
        result.profile.permanent_address = self.cleaned_data['permanent_address']

        if commit:
            result.profile.save()

        return result
