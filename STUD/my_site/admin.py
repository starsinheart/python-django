from django.contrib import admin
from . models import Group, Student, Mark, Discipline, StudentDisciplineMark   

# Register your models here.
admin.site.register(Group)
admin.site.register(Student)
admin.site.register(Mark)
admin.site.register(Discipline)
admin.site.register(StudentDisciplineMark)

