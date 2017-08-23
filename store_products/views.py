from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Product
from .forms import Contactform, Userform
from django.utils import timezone
from django.db.models import Max
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    viewed_products = []
    #display rank attribute used to denote which items end up in which row in bootstrap
    for r in Product.objects.values_list('display_rank', flat=True).distinct():
        x = Product.objects.filter(favorite=True, display_rank=r)
        viewed_products.append(x)
    return render(request, 'store_products/home.html', {'products': viewed_products})

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

def suits_view(request):
    return products_serializer(request, 'Suit')


def shirts_view(request):
    return products_serializer(request, 'Shirt')

def shoes_view(request):
    return products_serializer(request, 'Shoes')

def ties_view(request):
    return products_serializer(request, 'Tie')

def products_serializer(request, type):
    viewed_products = []
    product = type
    product = product.lower()
    for r in Product.objects.values_list('display_rank', flat=True).distinct():
        x = Product.objects.filter(type=type, display_rank=r)
        viewed_products.append(x)
    return render(request, ('store_products/{0}.html'.format(product)), {'products': viewed_products})

"""def suit_view(request):
    products_list = []
    maxid = Product.objects.aggregate(Max('id'))
    rows = maxid/4
    for row in range(0,rows):
        x = []
        for num in range((4*row),((4*row)+4)):
            x = Product.objects.filter(type='suit', id=num)
        products_list.append(x)


#def login(request):"""