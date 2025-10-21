from django.shortcuts import render

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация успешна! Ожидайте подтверждения.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'account/register.html', {'form': form})