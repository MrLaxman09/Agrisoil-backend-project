from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Signup
from .forms import SignupForm

# Signup
def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Signup successful! Please login now.")
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'Accounts/signup.html', {'form': form})


# Login
def login_view(request):
    if request.method == "POST":
        email = request.POST.get('user_email')
        password = request.POST.get('user_password')

        try:
            user = Signup.objects.get(user_email=email, user_password=password)
            request.session['user_id'] = user.id
            request.session['user_name'] = user.user_first_name
            messages.success(request, f"Welcome back, {user.user_first_name}!")
            return redirect('home')
        except Signup.DoesNotExist:
            messages.error(request, "Invalid email or password!")

    return render(request, 'Accounts/login.html')

# logout 
from django.shortcuts import redirect
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('home')  # Replace 'home' with your homepage URL name



# Home (dummy home page)
def home_view(request):
    if 'user_id' in request.session:
        name = request.session.get('user_name')
        return render(request, 'Accounts/home.html', {'name': name})
    else:
        return redirect('login')
