from django.shortcuts import render, redirect

from item.models import Category, Item

from .forms import SignupForm

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "User creation successful")
            return redirect('/login/')
    else:
        form = SignupForm()

    messages.success(request, "User creation failed, try again")
    return render(request, 'core/signup.html', {
        'form': form
    })

@login_required
def logout_user(request):
    logout(request)
    messages.success(request, "Logout successful")
    return redirect("/")
