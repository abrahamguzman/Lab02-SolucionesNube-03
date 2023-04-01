from django.shortcuts import render
from .models import Juguete

# Create your views here.
def index(request):
    juguetes = Juguete.objects.all()
    return render(request, 'index.html', {'juguetes': juguetes})