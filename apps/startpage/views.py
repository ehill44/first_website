from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.validators import validate_email
from .models import User
import bcrypt

def index(request):
    request.session.flush()
    return render(request, 'startpage/index.html')

def process1(request):
    errors=User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect(reverse('startpage:index'))
    else:
        new_user = User.objects.create(first_name=request.POST['first_name'],
            user_name = request.POST['user_name'], 
            date_hired = request.POST['date_hired'],
            password = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt()))
        new_user.save()
        request.session['current_user']= new_user.id
    return redirect('wish_list:index')

def process2(request):
        if User.objects.filter(user_name=request.POST['user_name']):
            users = User.objects.get(user_name=request.POST['user_name'])
            if request.POST['user_name'] == users.user_name and bcrypt.checkpw(request.POST['password'].encode(), users.password.encode()):
                request.session['current_user'] = users.id
                return redirect(reverse('wish_list:index'))
            elif request.POST['user_name']!= users.user_name or request.POST['password']!=users.password:
                logerror={ 
                'issue': "Something's not right. Make sure you have the right password"
                }
                for tag, error in logerror.iteritems():
                    messages.error(request, error, extra_tags=tag)
                    return redirect(reverse('startpage:index'))
        else:
            logerror2={
                'issue': "Something's not right. Check your information" 
            }
            for tag, error in logerror2.iteritems():
                    messages.error(request, error, extra_tags=tag)
            return redirect(reverse('startpage:index'))
   
    
