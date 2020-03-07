from django.http import Http404
from django.shortcuts import render

from .models import GmValue

# Create your views here.

def category(request):
    try:
        gm_val=GmValue.objects.all()
    except GmValue.DoesNotExist:
        raise Http404('No Value Found')    
    return render(request,'gm/index.html',{'gmval':gm_val})

