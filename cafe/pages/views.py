from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("Hello world")
    return render(request,'pages/index.html')
def about(request):
    students = {'tom': 90, 'harry' : 80, 'jarry' : 60, 'merry': 40}
    context = {'context' : students}
    
    return render(request,'pages/about.html',context)
def Contact_us(request):
    return render(request,'pages/Contact_us.html')