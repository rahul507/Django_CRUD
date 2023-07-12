#-*- coding:utf-8 -*-
from .models import Task
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
        'password': forms.PasswordInput(),
    }
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.initial['password'] = 'default_password'
        self.fields['password'].required = False

    def save(self, commit=True):
        task = super(TaskForm, self).save(commit=False)
        if not task.password:
            task.password = 'default_password'
        if commit:
            task.save()
        return task

class MyForm(forms.Form):
    driver_email = forms.CharField()
    driver_password= forms.CharField()


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
