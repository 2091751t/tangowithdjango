from django.shortcuts import render
from rango.models import Category
from rango.models import Page

from django.http import HttpResponse

def index(request):

    category_list = Category.objects.order_by('-likes')[:5]
    pages_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list, 'pages': pages_list}

    return render(request, 'rango/index.html', context_dict)

def about(request):
    context_dict = {'boldmessage': "This tutorial was completed\
                    by Nelly Temelkova - 2091751T"}

    return render(request, 'rango/about.html', context_dict)

def category(request, category_name_slug):

    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        pages = Page.objects.filter(category=category)


        context_dict['pages'] = pages

        context_dict['category'] = category
    except Category.DoesNotExist:

        pass

    return render(request, 'rango/category.html', context_dict)
