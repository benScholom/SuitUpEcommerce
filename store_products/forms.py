from django.forms import ModelForm
from .models import Messages

class Contactform(ModelForm):
    class Meta:
        model = Messages
        fields = ['first_name', 'last_name', 'email', 'text']
