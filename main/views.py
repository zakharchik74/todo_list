import re
from xml.dom.domreg import well_known_implementations
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import ToDo, ToDo_process, ToDo_completed
from django.contrib.auth.models import User

def index(request):
    if request.user.is_authenticated:
        todo = ToDo.objects.filter(user=request.user)
        todo_process = ToDo_process.objects.filter(user=request.user)
        todo_completed = ToDo_completed.objects.filter(user=request.user)
        if request.method == 'POST':
            ListPr = request.POST.getlist('process')
            for i in range(len(ListPr)):
                todopr_id, todopr_todo = ListPr[i].split(".")
                new_record = ToDo_process.objects.create(to_do=todopr_todo, user=request.user)
                new_record.save()
                todo_del = ToDo.objects.get(id=todopr_id)
                todo_del.delete()

            CompPr = request.POST.getlist('completed')
            for i in range(len(CompPr)):
                todocom_id, todocom_todo = CompPr[i].split(".")
                new_record = ToDo_completed.objects.create(to_do=todocom_todo, user=request.user)
                new_record.save()
                todo_del = ToDo_process.objects.get(id=todocom_id)
                todo_del.delete() 

            return redirect('index')
        else:
            return render(request, 'index.html', {'todo' : todo, 'process' : todo_process, 'completed' : todo_completed})
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
    todo = ToDo_completed.objects.get(id=id)
    todo.delete()
    return redirect('index')
