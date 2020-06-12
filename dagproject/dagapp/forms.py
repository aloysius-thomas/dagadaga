from django.contrib.auth.forms import UserCreationForm
from . models import User
from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = {
            "username",
            "first_name",
            "last_name",
            "username",
            "phone",
            "email",
        }

