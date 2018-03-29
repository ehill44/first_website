from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.validators import validate_email
from ..startpage.models import User
from .models import Product
from django.db.models import Q


def index(request):
    context={
        'display_name': User.objects.get(id=request.session['current_user']),
        'your_list':Product.objects.filter(added_by=request.session['current_user']),
        'shared_item':Product.objects.filter(others=request.session['current_user']),
        'all_items': Product.objects.filter(~Q(added_by=request.session['current_user'])).exclude(others=request.session['current_user'])
    }
    return render(request, 'wish_list/index.html', context)

def process1(request):
    errors2 = Product.objects.validator(request.POST)
    if len(errors2):
        for tag, error in errors2.iteritems():
            messages.error(request, error, extra_tags=tag)
            return redirect(reverse('wish_list:create'))
    else:
        current_user = User.objects.get(id=request.session['current_user'])
        new_item = Product.objects.create(item=request.POST['item'],added_by=current_user)
        new_item.save()
    return redirect(reverse('wish_list:index'))

def process2(request):
    if request.POST['delete']:
        this_item = Product.objects.get(id=request.POST['delete'])
        this_item.delete()
    return redirect(reverse('wish_list:index'))

def process3(request):
    if request.POST['remove']:
        this_item = Product.objects.get(id=request.POST['remove'])
        this_item.others.remove(request.session['current_user'])
    return redirect(reverse('wish_list:index'))

def process4(request):
    if request.POST['add']:
        this_user = User.objects.get(id=request.session['current_user'])
        this_item = Product.objects.get(id=request.POST['add'])
        this_item.others.add(this_user)
        return redirect(reverse('wish_list:index'))

def create(request):
    return render(request, 'wish_list/create.html')

def show(request, id):
    context={
        'current_item': Product.objects.get(id=id)
    }
    return render(request, 'wish_list/show.html', context)
