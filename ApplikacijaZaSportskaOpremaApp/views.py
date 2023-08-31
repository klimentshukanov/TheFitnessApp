from django.shortcuts import render, redirect

from .models import *
from .forms import *


# Create your views here.


def index(request):
    queryset = Produkt.objects.all()[:3]
    context = {"products": queryset}
    return render(request, "index.html", context=context)


def products(request):
    queryset = Produkt.objects.all()
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
            return redirect("products")

    return render(request, "add.html", context={"form": ProduktForm})