from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import *
from .forms import *


# Create your views here.


def index(request):
    queryset = Produkt.objects.all()[:3]
    context = {"products": queryset}
    return render(request, "index.html", context=context)


def categories(request):
    queryset = Category.objects.all()
    context = {"categories": queryset}
    return render(request, "categories.html", context=context)


def products(request, id=0):
    if id == 0:
        return render(request, "categories.html")
    else:
        queryset = Produkt.objects.filter(category=id)
        context = {"products": queryset}
        return render(request, "products.html", context=context)


def add(request):
    if request.method == "POST":
        form_data = ProduktForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            produkt = form_data.save(commit=False)
            produkt.user = request.user
            produkt.image = form_data.cleaned_data['image']
            produkt.save()
            return redirect("categories")

    return render(request, "add.html", context={"form": ProduktForm})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, "There Was An Error Logging In, Try Again...")
            return redirect('login_user')

    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You Were Logged Out!")
    return redirect('index')


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration Successful!")
            return redirect('index')
    else:
        form = RegisterUserForm()

    return render(request, 'register.html', {
        'form': form,
    })


def details(request, id=0):
    if id == 0:
        return render(request, "products.html")
    else:
        produkt = Produkt.objects.get(pk=id)
        context = {"produkt": produkt}
        return render(request, "details.html", context=context)


def cart(request):
     return render(request, "cart.html")
