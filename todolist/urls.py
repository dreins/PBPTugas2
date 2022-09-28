from django.urls import path
from todolist.views import delete, show_task, register, login_user, logout_user, create_task, update, delete

app_name = 'todolist'

urlpatterns = [
    path('', show_task, name='show_task'),
    path('login/', login_user, name='login_user'),
    path('register/', register, name='register'),
    path('create-task/', create_task, name='create_task'),
    path('logout/', logout_user, name='logout_user'),
    path('update-task/<int:key>/', update, name='update'),
    path('delete-task/<int:key>/', delete, name='delete'),
]