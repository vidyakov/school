from django.contrib.auth.forms import UserCreationForm

from authapp.models import SchoolUser


class SchoolUserCreationForm(UserCreationForm):
    class Meta:
        model = SchoolUser
        fields = 'username', 'email', 'password1', 'password2'
