from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import MyUser


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in ['username', 'password']:
            self.fields[field].help_text = None


class UserForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['username', 'password1', 'password2']

# to remove help text from user form (like: password must be 8 char)
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in ['username', 'password1', 'password2']:
            self.fields[field].help_text = None


# validations for match two fields value (password == re_enter_password)
    # def clean(self):
    #     super().clean()
    #     print(self.cleaned_data)
    #     pass1 = self.cleaned_data['password1']
    #     pass2 = self.cleaned_data['password_confirmation']
    #     if pass1 != pass2:
    #         print('hiiiiiiiiiiiiiiiii')
    #         raise forms.ValidationError('Password dose Not Match')
