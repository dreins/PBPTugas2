from django.shortcuts import render, redirect
from todolist.forms import TodoForm
from todolist.models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_task(request):
    data_task = Task.objects.all()
    context = {
        'username': request.COOKIES['username'],
        'last_login': request.COOKIES['last_login'],
        'mytodo': data_task,
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login_user')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) 
            response = HttpResponseRedirect(reverse("todolist:show_task")) 
            response.set_cookie('username', username) 
            response.set_cookie('last_login', str(datetime.datetime.now())) 
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login_user'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def create_task(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            formdata = form.save(commit=False)
            formdata.user = request.user
            formdata.save()
            return HttpResponseRedirect(reverse('todolist:show_task'))
    else:
        messages.info(request, 'Silahkan masukkan to do anda!')
        
    return render(request, 'create_task.html', {'form': form})

@login_required(login_url='/todolist/login/')
def update(request, key):
    mytask = Task.objects.get(user = request.user,pk = key)
    mytask.is_finished = not(mytask.is_finished)
    mytask.save()
    return redirect('todolist:show_task')

@login_required(login_url='/todolist/login/')
def delete(request, key):
    mytask = Task.objects.get(user = request.user,pk = key)
    mytask.delete()
    return redirect('todolist:show_task')
