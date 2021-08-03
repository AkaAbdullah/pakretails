from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class myUserCreationForm(UserCreationForm):

    class Meta:
        model=User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(myUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'input'
        self.fields['password1'].widget.attrs['class'] = 'input'
        self.fields['password2'].widget.attrs['class'] = 'input'

class myLoginForm(AuthenticationForm):

    class Meta:
        model=User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(myLoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'input'
        self.fields['password'].widget.attrs['class'] = 'input'