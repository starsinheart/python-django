from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .forms import UserRegistrationForm, UserLoginForm
from .models import User, StudentProfile, TeacherProfile
from my_site.models import Student, StudentDisciplineMark

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Регистрация успешна! Ожидайте подтверждения администратором.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'account/register.html', {'form': form})


class CustomLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'account/login.html'
    
    def form_valid(self, form):
        user = form.get_user()
        if not user.is_approved and not user.is_admin():
            messages.error(self.request, 'Ваш аккаунт еще не подтвержден администратором.')
            return redirect('login')
        return super().form_valid(form)


@login_required
def profile(request):
    user = request.user
    context = {'user': user}
    
    if user.is_student():
        try:
            student_profile = StudentProfile.objects.get(user=user)
            if student_profile.student:
                # Получаем успеваемость студента
                marks = StudentDisciplineMark.objects.filter(student=student_profile.student)
                context['marks'] = marks
                context['student'] = student_profile.student
        except StudentProfile.DoesNotExist:
            messages.info(request, 'Профиль студента не найден. Обратитесь к администратору.')
        except Exception as e:
            messages.error(request, f'Ошибка при загрузке данных: {str(e)}')
    
    return render(request, 'account/profile.html', context)


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Вы успешно вышли из системы.')
    return redirect('home')