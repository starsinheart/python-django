from django.db import models
from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):
#     class Role(models.TextChoices):
#         ADMIN = "ADMIN", "Администратор"
#         TEACHER = "TEACHER", "Преподаватель"
    
#     role = models.CharField(
#         max_length=20, 
#         choices=Role.choices, 
#         default=Role.TEACHER
#     )
#     is_approved = models.BooleanField(
#         default=False,
#         verbose_name="Подтвержден"
#     )
    
#     def save(self, *args, **kwargs):
#         if self.is_superuser:
#             self.role = self.Role.ADMIN
#             self.is_approved = True
#         super().save(*args, **kwargs)

# class TeacherProfile(models.Model):
#     user = models.OneToOneField(
#         User, 
#         on_delete=models.CASCADE,
#         limit_choices_to={'role': User.Role.TEACHER}
#     )

#     def __str__(self):
#         return f"Преподаватель: {self.user.get_full_name()}"