from dataclasses import field, fields
from django.forms import ModelForm
from .models import Room, User
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2' ]

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']   # for exluding specific Form fields from the all fields

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [ 'avatar', 'name', 'username', 'email', 'bio']