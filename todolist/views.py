from django.shortcuts import render, redirect, get_object_or_404
from todolist.models import Task
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse

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

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        user_exist = User.objects.filter(username=username).exists()
        if password != confirm_password:
            messages.info(request, 'Confirm Password doesn\'t match!')
        elif user_exist:
            messages.info(request, 'User already registered!')
        elif not user_exist:
            user = User.objects.create_user(username=username, password=confirm_password)
            if user == None:
                messages.info(request, 'Try again!')
            else:
                user.save()
                return redirect('todolist:login_user')
        else:
            messages.info(request, 'Try again!')

    return render(request, 'register.html')

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
    if request.method == 'POST':
        user = request.user
        title = request.POST.get('title')
        description = request.POST.get('description')
        task = Task.objects.create(user = user, title = title, description = description)
        task.save()
        if task == None:
            messages.info(request, 'Silahkan masukkan to do anda!')
        else:
            return redirect('todolist:show_task')
        
    return render(request, 'create_task.html')

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

@login_required(login_url='/todolist/login/')
@csrf_exempt
def create_task_ajax(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST.get('title')
        description = request.POST.get('description')
        task = Task.objects.create(user = user, title = title, description = description)
        if task == None:
            messages.info(request, 'Silahkan masukkan to do anda!')
        else:
            return JsonResponse({'message : Task Created!'})
        
    return JsonResponse({'message : Task Updated!'})

def show_json(request):
    data = Task.objects.filter(user=request.user).order_by('id')

    return HttpResponse(
        serializers.serialize("json", data), 
        content_type="application/json"
    )

@login_required(login_url='/todolist/login/')
@csrf_exempt
def update_ajax(request, key):
    if request.method == 'POST':
        mytask = get_object_or_404(Task, user = request.user, pk = key)
        mytask.is_finished = not(mytask.is_finished)
        mytask.save()

    return JsonResponse({'error': False})

@login_required(login_url='/todolist/login/')
@csrf_exempt
def delete_ajax(request, key):
    if request.method == 'POST':
        mytask = get_object_or_404(Task, user = request.user, pk = key)
        mytask.delete()
        
    return JsonResponse({'error': False})


