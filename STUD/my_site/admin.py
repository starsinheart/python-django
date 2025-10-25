from django.contrib import admin
from .models import Group, Student, Mark, Discipline, StudentDisciplineMark

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'middle_name', 'group')
    list_filter = ('group',)
    search_fields = ('name', 'last_name', 'middle_name')

@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(StudentDisciplineMark)
class StudentDisciplineMarkAdmin(admin.ModelAdmin):
    list_display = ('student', 'discipline', 'mark')
    list_filter = ('discipline', 'mark')
    search_fields = ('student__name', 'student__last_name', 'discipline__name')

