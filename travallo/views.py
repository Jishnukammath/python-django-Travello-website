from travallo.models import Destination
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.
def index(request):
    obj=Destination.objects.all()
    return render(request,'index.html',{'objs':obj})

