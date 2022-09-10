from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
data_katalog = CatalogItem.objects.all()

def katalog(request):
    context = {
    'katalog_items': data_katalog,
    'nama': 'Davyn Reinhard',
    'student_id': '2106751083'
    }
    return render(request, 'katalog.html', context)
