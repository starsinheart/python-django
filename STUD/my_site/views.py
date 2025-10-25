from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from .forms import StudentForm
from .models import Student

# Create your views here.
def home(request):
    context={}
    return render(request,'my_site/home.html',context)

def about(request):
    context={}
    return render(request,'my_site/about.html',context)

def services(request):
    context={}
    return render(request,'my_site/services.html',context)

def contacts(request):
    context={}
    return render(request,'my_site/contacts.html',context)

def is_teacher_or_admin(user):
    return user.is_authenticated and (user.is_teacher() or user.is_admin())

def is_admin(user):
    return user.is_authenticated and user.is_admin()

@login_required
@user_passes_test(is_teacher_or_admin)
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students_list')
    else:
        form = StudentForm()
    return render(request, 'my_site/add_students.html', {'form': form})

@login_required
@user_passes_test(is_teacher_or_admin)
def students_list(request):
    students = Student.objects.all()
    return render(request, 'my_site/students_list.html', {'students':students})
