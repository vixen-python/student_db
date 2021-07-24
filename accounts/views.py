from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView

from accounts.forms import SignUpForm, MeForm


class SubmittableLogoutView(TemplateView):
    template_name = 'registration/logged_out.html'


class SignUpView(CreateView):
    template_name = "form.html"
    form_class = SignUpForm
    success_url = reverse_lazy('index')


class MeView(LoginRequiredMixin, UpdateView):
    template_name = 'form.html'
    model = User
    form_class = MeForm
    success_url = reverse_lazy('accounts:me')

    def get_object(self, queryset=None):
        return self.request.user

    def get_initial(self):
        result = super().get_initial()
        result['personal_phone'] = self.request.user.profile.personal_phone
        result['permanent_address'] = self.request.user.profile.permanent_address
        return result
