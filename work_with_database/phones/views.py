from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_pages = request.GET.get("sort")
    if sort_pages == 'name':
        phone_objects = Phone.objects.order_by('name')
        context = {
            'phones': phone_objects
        }
        return render(request, template, context)
    elif sort_pages == 'min_price':
        phone_objects = Phone.objects.order_by('price')
        context = {
            'phones': phone_objects
        }
        return render(request, template, context)
    elif sort_pages == 'max_price':
        phone_objects = Phone.objects.order_by('-price')
        context = {
            'phones': phone_objects
        }
        return render(request, template, context)
    else:
        phone_objects = Phone.objects.all()
        context = {
            'phones': phone_objects
        }
        return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug__contains=slug).first()
    context = {
        'phone': phone
    }
    return render(request, template, context)
