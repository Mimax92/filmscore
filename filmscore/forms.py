from django.forms import ModelForm
from .models import Film, ExtraInfo, Rating
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.contrib.auth import get_user_model


class FilmForm(ModelForm):
    class Meta:
        def __init__(self, *args, **kwargs):
            super(FilmForm, self).__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })

        model = Film
        fields = ['title', 'year', 'description', 'premiere', 'imdb_rating', 'poster']
        Recepient = forms.ChoiceField(label=u'Recepient', widget=forms.Select(attrs={'id': 'combobox'}))


def validate_user(value):
    if get_user_model().objects.filter(username=value).exists():
        raise ValidationError('Username already exists')


class ExtraInfoForm(ModelForm):
    class Meta:
        def __init__(self, *args, **kwargs):
            super(ExtraInfoForm, self).__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })

        model = ExtraInfo
        fields = ['runtime', 'genres']


class CreateUserForm(forms.Form):
    username = forms.CharField(max_length=64, validators=[validate_user], label='Username')
    password = forms.CharField(max_length=32, widget=forms.PasswordInput, label='Password')
    repeated_password = forms.CharField(max_length=32, widget=forms.PasswordInput, label='Repeat password')
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)
    email = forms.EmailField(validators=[EmailValidator()])

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        repeated_password = cleaned_data.get('repeated_password')
        if cleaned_data['password'] != cleaned_data['repeated_password']:
            raise forms.ValidationError('The passwords provided are different')


class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ['stars', 'review']
