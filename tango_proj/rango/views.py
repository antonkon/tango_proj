from django.shortcuts import render
from tango_proj.rango.models import Category, Page


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]

    content = {'categories': category_list}
    content['message'] = 'hello'
    return render(request, 'rango/index.html', content)

def about(request):
    return render(request, 'rango/about.html')

def category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        pages = Page.objects.filter(category=category)[:5]
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass

    return render(request,'rango/category.html',context_dict)