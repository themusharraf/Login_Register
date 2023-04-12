from django.contrib.auth.forms import UserCreationForm

from apps.models import Users


class UserForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ('username', 'email', 'password1')

