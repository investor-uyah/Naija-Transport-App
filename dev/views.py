from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
# from django_ratelimit.decorators import ratelimit
from django.contrib import auth
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()

@login_required
def home(request):
    return render(
        request,
        'welcome.html'
    )

# @ratelimit(key='ip', rate='3/m', block=True)
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid login credentials")
            return redirect("login")
    return render(request, "registration/login.html")
    
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/accounts/login/")

# @ratelimit(key='ip', rate='1/m', block=True)
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})