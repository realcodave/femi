from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class NewUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required. 30 characters or fewer.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required. 30 characters or fewer.')
    phone_number = forms.CharField(max_length=30, required=True, help_text='Required. 30 characters or fewer.')

    class Meta:
        model = CustomUser
        fields = ("username", "first_name", "last_name", "email", "account_type", "phone_number", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user