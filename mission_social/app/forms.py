from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, UserProfile2


class ExtendedUserCreationForm(UserCreationForm):

    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter the E-mail ID'
               }))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user


class UserProfileForm(forms.ModelForm):

    choices = [
        ('Male', 'male'),
        ('Female', 'Female'),

    ]

    gender = forms.ChoiceField(required=True, choices=choices, widget=forms.Select(
        attrs={'class': 'form-control'}))

    contact = forms.IntegerField(max_value=10000000000, required=True, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': "Enter the Contact"}))

    class Meta:
        model = UserProfile
        fields = {'contact', 'gender'}



class ExtendedUserCreationForm2(UserCreationForm):

    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter the E-mail ID'
               }))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user


class UserProfileForm2(forms.ModelForm):

    choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),

    ]

    gender = forms.ChoiceField(required=True, choices=choices, widget=forms.Select(
        attrs={'class': 'form-control'}))

    contact = forms.IntegerField(max_value=10000000000, required=True, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': "Enter the Contact"}))

    class Meta:
        model = UserProfile2
        fields = {'gender', 'contact'}
