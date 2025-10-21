from django.shortcuts import render, redirect
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

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students_list')
    else:
        form = StudentForm()
    return render(request, 'my_site/add_students.html', {'form': form})

def students_list(request):
    students = Student.objects.all()
    return render(request, 'my_site/students_list.html', {'students':students})
