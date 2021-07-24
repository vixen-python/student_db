from django.contrib.auth.mixins import UserPassesTestMixin


class FacultyWorkerRequired(UserPassesTestMixin):
    def test_func(self) -> bool:
        return self.request.user.email.endswith('@cvut.cz')
