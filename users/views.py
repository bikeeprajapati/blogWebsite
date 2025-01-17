from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib.auth import logout


# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-index')
            
    else:
        form = SignUpForm()
    context ={
        'form': form,
    }
    return render(request, 'users/sign_up.html', context)
def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')

def profile(request):
    return render(request, 'users/profile.html')
