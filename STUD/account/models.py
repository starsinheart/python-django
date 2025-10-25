from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Администратор"
        TEACHER = "TEACHER", "Преподаватель"
        STUDENT = "STUDENT", "Студент"
    
    role = models.CharField(
        max_length=20, 
        choices=Role.choices, 
        default=Role.STUDENT,
        verbose_name="Роль"
    )
    is_approved = models.BooleanField(
        default=False,
        verbose_name="Подтвержден"
    )
    
    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.role = self.Role.ADMIN
            self.is_approved = True
        super().save(*args, **kwargs)

    def is_admin(self):
        return self.role == self.Role.ADMIN
    
    def is_teacher(self):
        return self.role == self.Role.TEACHER
    
    def is_student(self):
        return self.role == self.Role.STUDENT
    
    @property
    def is_admin_property(self):
        return self.role == self.Role.ADMIN
    
    @property
    def is_teacher_property(self):
        return self.role == self.Role.TEACHER
    
    @property
    def is_student_property(self):
        return self.role == self.Role.STUDENT


class StudentProfile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        limit_choices_to={'role': User.Role.STUDENT}
    )
    student = models.ForeignKey('my_site.Student', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"Профиль студента: {self.user.get_full_name()}"


class TeacherProfile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        limit_choices_to={'role': User.Role.TEACHER}
    )

    def __str__(self):
        return f"Профиль преподавателя: {self.user.get_full_name()}"