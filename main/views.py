import re
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import ToDo
from django.contrib.auth.models import User

def index(request):
    user = request.user
    if user.is_authenticated:
        data  = ToDo.objects.filter(user=user)
        return render(request, 'index.html', {'todo' : data})
    else:
        return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def newtodo(request):
    if request.method == 'POST':
        todo = request.POST['todo']
        user = request.user
        new_record = ToDo.objects.create(to_do=todo, user=user)
        new_record.save()
        return redirect('/')
    else:
        return render(request, 'newtodo.html')

def delete(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect('/')
