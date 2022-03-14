from turtle import title
from unicodedata import category
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Product
from django.urls import reverse


def main(request):
    product_list = Product.objects.all()
    return render(request, 'main.html', {'product_list':product_list})

def detail_view(request, id):
    single_products = Product.objects.get(id=id)
    return render(request, 'single_product.html', {'single_products':single_products})

def delete_view(request, id):
    delete_news = Product.objects.get(id=id)
    delete_news.delete()
    return HttpResponse("Запись удалена!")


def create_view(request):
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, 'create_product.html', {'categories':categories})

    if request.method == "POST":
        name_prod = request.POST.get("name_prod")
        inv_number = request.POST.get("inv_number")
        start_price = request.POST.get("start_price")
        rem_price = request.POST.get("rem_price")
        category_id = request.POST.get("category")

        category = Category.objects.get(id=category_id)

        new_products = Product(name_prod=name_prod, inv_number=inv_number, start_price=start_price, rem_price=rem_price, category_prod=category)
        new_products.save()

        return redirect(reverse("all_product"))


def update_view(request, id):

    single_products = Product.objects.get(id=id)

    if request.method == "GET":
        categories = Category.objects.all()

        context = {
            "categories":categories,
            "single_products": single_products,
        }

        return render(request, 'update_product.html', context)

    if request.method == "POST":
        name_prod = request.POST.get("name_prod")
        inv_number = request.POST.get("inv_number")
        start_price = request.POST.get("start_price")
        rem_price = request.POST.get("rem_price")
        category_id = request.POST.get("category")

        category = Category.objects.get(id=category_id)

        single_products.name_prod = name_prod
        single_products.inv_number = inv_number
        single_products.start_price = start_price
        single_products.rem_price = rem_price
        single_products.category = category
        single_products.save()

        return redirect(reverse("all_product"))
