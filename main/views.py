import re
from xml.dom.domreg import well_known_implementations
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import ToDo
from django.contrib.auth.models import User

def index(request):
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
            ListPr = request.POST.getlist('process')
            for i in ListPr:
                StatusPr = ToDo.objects.get(id=i)
                StatusPr.status = 'process'
                StatusPr.save()

            ListComp = request.POST.getlist('completed')
            for i in ListComp:
                StatusComp = ToDo.objects.get(id=i)
                StatusComp.status = 'completed'
                StatusComp.save()
            return redirect('index')
        else:
            todo = ToDo.objects.filter(user=user, status='todo')
            process = ToDo.objects.filter(user=user, status='process')
            completed = ToDo.objects.filter(user=user, status='completed')
            return render(request, 'index.html', {'todo' : todo, 'process' : process, 'completed' : completed})
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
        return redirect('index')
    else:
        return render(request, 'newtodo.html')

def delete(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect('index')
