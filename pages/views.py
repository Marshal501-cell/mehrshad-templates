from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .models import ContactMessage


def home(request):
    return render(request, 'pages/home.html')


def contact(request):
    error = ''
    name = ''
    email = ''
    message = ''
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()
        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            request.session['contact_sent'] = True
            return redirect('contact')
        error = 'همه فیلدها را کامل کنید.'
    sent = request.session.pop('contact_sent', False)
    return render(request, 'pages/contact.html', {'sent': sent, 'error': error, 'name': name, 'email': email, 'message': message})


def register(request):
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        if not username or not password1:
            error = 'نام کاربری و رمز عبور را وارد کنید.'
        elif password1 != password2:
            error = 'رمز عبور و تکرار آن یکی نیست.'
        elif User.objects.filter(username=username).exists():
            error = 'این نام کاربری قبلا ثبت شده است.'
        else:
            User.objects.create_user(username=username, password=password1)
            return redirect('login')
    return render(request, 'pages/register.html', {'error': error})


def login_view(request):
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        error = 'نام کاربری یا رمز عبور درست نیست.'
    return render(request, 'pages/login.html', {'error': error})


def about(request):
    return render(request, 'pages/about.html')
