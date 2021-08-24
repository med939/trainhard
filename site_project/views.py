from django.shortcuts import render
from .models import Item
from django.core.paginator import Paginator



def base(request):
    
    return render(request, 'lrn/base.html')

def Search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        items = Item.objects.filter(title__contains = searched)
        paginator = Paginator(items, 40) 

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'lrn/search.html', {'page_obj':page_obj, 'searched':searched})
    else:
        return render(request, 'lrn/search.html', {})

def home(request):
    items = Item.objects.all()
    paginator = Paginator(items, 40) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {'items':items, 'page_obj':page_obj}
    return render(request, 'lrn/home.html', context)

def Produit(request, pk):
    item = Item.objects.get(id = pk)
    context = {'item':item}
    return render(request, 'lrn/produit.html', context)


def Parfum_h(request):
    items = Item.objects.filter(category='Parfum homme')
    paginator = Paginator(items, 40) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'items':items, 'page_obj':page_obj
    }
    return render(request, 'lrn/parfum_h.html', context)

def Parfum_f(request):
    items = Item.objects.filter(category='Parfum femme')
    paginator = Paginator(items, 40) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'items':items, 'page_obj':page_obj}
    
    return render(request, 'lrn/parfum_f.html', context)

def Maquillage(request):
    items = Item.objects.filter(category='Maquillage')
    paginator = Paginator(items, 40) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'items':items, 'page_obj':page_obj
    }
    return render(request, 'lrn/maquillage.html', context)
