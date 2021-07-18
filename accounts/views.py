from django.views.generic import TemplateView


class SubmittableLogoutView(TemplateView):
    template_name = 'registration/logged_out.html'
