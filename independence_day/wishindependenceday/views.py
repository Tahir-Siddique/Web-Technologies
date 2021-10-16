from django.shortcuts import render
from datetime import datetime
# Create your views here.

def index(request,name):
    now = datetime.now()
    context = {
        "name":name.capitalize(),
        "isIndependence": now.month==8 and now.day==14
    }
    return render(request,'wishindependenceday/index.html',context)