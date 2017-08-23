from django.forms import ModelForm, forms
from .models import Messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Contactform(ModelForm):
    class Meta:
        model = Messages
        fields = ['first_name', 'last_name', 'email', 'text']

class Userform(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name']
    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])




