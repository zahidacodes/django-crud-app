from django.shortcuts import render,HttpResponseRedirect
from .forms import myform
from .models import myclass
# Create your views here.
def readandinsert(request):
    if request.method == "POST":
        fm = myform(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data["name"]
            email = fm.cleaned_data["email"]
            password = fm.cleaned_data["password"]
            em = myclass(name=name,email=email,password=password)
            em.save() 
            fm = myform()
    else:
        fm = myform()
    data = myclass.objects.all()
    return render(request,"readrecord.html",{"form":fm,"data":data})

# update the record 
def modify(request,id):
    if request.method == "POST": 
        stu = myclass.objects.get(pk=id)
        fm = myform(request.POST,instance=stu)
        if fm.is_valid(): 
            fm.save()
    else:
        stu = myclass.objects.get(pk=id)
        fm = myform(instance=stu)
    return render(request,"uprecord.html",{"form":fm})



# delete the record 
def destroy(request,id):
    if request.method == "POST":
        stu = myclass.objects.get(pk=id)
        stu.delete()
        return HttpResponseRedirect('/')