from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context={}
    return render(request,'base/calci.html',context)
def profile(request):
    return HttpResponse("profile")
def calci(request):
    if request.method=='POST':
        numberone=request.POST.get("number one")
        numbertwo=request.POST.get("number two")
        operation=request.POST.get("operation")
        if operation=="add":
            result=float(numberone)+float(numbertwo)
            context={'result':result}
            return render(request,"base.calci.html",context)
        elif operation=="sub":
            result=float(numberone)-float(numbertwo)
            context={'result':result}
            return render(request,"base.calci.html",context)
        elif operation=="multiplication":
            result=float(numberone)*float(numbertwo)
            context={'result':result}
            return render(request,"base.calci.html",context)
        elif operation=="div":
            result=float(numberone)/float(numbertwo)
            context={'result':result}
            return render(request,"base.calci.html",context)
        
            
            