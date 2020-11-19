from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<em>My second proj </em>")

def help(request):
    helpDict={'help_insert':'HElp Page'}
    return render(request,'appTwo/help.html',context=helpDict)