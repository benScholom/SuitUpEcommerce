from django.shortcuts import render, redirect
from .models import Product
from .forms import Contactform, Userform
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    favorite_products = []
    #display rank attribute used to denote which items end up in which row in bootstrap
    for r in Product.objects.values_list('display_rank', flat=True).distinct():
        x = Product.objects.filter(favorite=True, display_rank=r)
        favorite_products.append(x)
    return render(request, 'store_products/home.html', {'products': favorite_products})

def about(request):
    return render(request, 'store_products/about.html')

def contact(request):
    form = Contactform(request.POST or None)
    title = "Contact"
    if form.is_valid():
        comment = form.save(commit=False)
        comment.date = timezone.now()
        comment.save()
        title = "Thanks for contacting us, we will get back to you shortly."
        form = None
        return render(request, 'store_products/contact.html', {"form": form, "title": title})
    return render(request, 'store_products/contact.html', {'form': form, "title": title})

def register(request):
    if request.method == 'POST':
        form = Userform(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'],)
            login(request, new_user)
            return redirect('home')
    else:
        form = Userform()
    return render(request, "registration/register.html", {'form': form})

def user_logout(request):
    logout(request)
    return render(request, 'registration/logout.html')


#def login(request):