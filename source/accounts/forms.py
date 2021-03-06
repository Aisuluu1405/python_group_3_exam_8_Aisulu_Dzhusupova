from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import widgets

from accounts.models import Profile


class UserCreationForm(forms.ModelForm):
    username = forms.CharField(max_length=100, label='Username', required=True)
    password = forms.CharField(label='Пароль', strip=False, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput, strip=False)
    email = forms.EmailField(label='Email', required=True)

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Passwords do not match!')
        return password_confirm

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            User.objects.get(email=email)
            raise ValidationError('User with this email already exists',
                                  code='user_email_exists')
        except User.DoesNotExist:
            return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            User.objects.get(username=username)
            raise ValidationError('User with this username already exists',
                                  code = 'user_username_exists')
        except User.DoesNotExist:
            return username

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm', 'email']


class UserChangeForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, label='First name', required=False)
    last_name = forms.CharField(max_length=100, label='Last name', required=False)
    avatar = forms.ImageField(label='User pic', required=False)
    email = forms.EmailField(label='Email', required=True)

    def get_initial_for_field(self, field, field_name):
        if field_name in self.Meta.profile_fields:
            return getattr(self.instance.user_profiles, field_name)
        return super().get_initial_for_field(field, field_name)

    def save(self, commit=True):
        user = super().save(commit=commit)
        user.user_profiles = self.save_profile(commit)
        return user

    def save_profile(self, commit=True):
        user_profiles, _ = Profile.objects.get_or_create(user=self.instance)
        for field in self.Meta.profile_fields:
            setattr(user_profiles, field, self.cleaned_data.get(field))
        if not user_profiles.avatar:
            user_profiles.avatar = None

        if commit:
            user_profiles.save()
        return user_profiles

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'avatar']
        profile_fields = ['avatar']
        labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'email': 'Email', 'avatar': 'Фото пользователя'}


class PasswordChangeForm(forms.ModelForm):
    password = forms.CharField(label='New Password', strip=False, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Confirm new Password', widget=forms.PasswordInput, strip=False)
    old_password = forms.CharField(label='Old Password', strip=False, widget=forms.PasswordInput)

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Passwords do not match!')
        return password_confirm

    def clean_old_password(self):
        old_password = self.cleaned_data.get("old_password")
        if not self.instance.check_password(old_password):
            raise forms.ValidationError('Old password is incorrect!')
        return old_password

    def save(self, commit=True):
        user = self.instance
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['password', 'password_confirm', 'old_password']

