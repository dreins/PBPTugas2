from django.urls import path
from katalog.views import katalog

app_name = 'katalog'

urlpatterns = [
    path('', katalog, name='katalog'),
]