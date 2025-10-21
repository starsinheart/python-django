from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, TeacherProfile

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = User.Role.TEACHER
        user.is_approved = False
        if commit:
            user.save()
            # Создаем пустой профиль
            TeacherProfile.objects.create(user=user)
        return user