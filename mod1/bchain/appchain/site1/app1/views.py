from django.shortcuts import render,get_object_or_404,redirect
from app1.models import Users
from app1.forms import Usersform,Userloginform
from django.http import HttpResponse,HttpResponseRedirect
import pandas
from django.contrib.auth import authenticate,get_user_model,login,logout
from django.contrib import messages

# Create your views here.
info = Users.objects.all()
def index(request):
    info = Users.objects.all()
    #db=pandas.DataFrame([[1,2,3],['jery',39,'nyc'],['bil',78,'La']],columns=['name','age','city'])

    context = {'info':info,'text':'helo text'}
    return render(request,'index.html',context)



def form_page(request):
    form = Usersform()
    if request.method == 'POST':
        form = Usersform(data=request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request,"succefuly registerd")
            return render(request,'index.html',{'info':info})
        else:
            return HttpResponse("not valid")
    return render(request,'base.html',{'form':form})

def page(request,id=None):
    u=Users.objects.all()
    inst = get_object_or_404(u,id=id)
    context = {'inst':inst}
    return render(request,'page1.html',context)


def login_view(request):
    form = Userloginform(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
    return render(request,'login.html',{"form":form})

def register(request):

    return render(request,'register.html',{})


def logout_view(request):
    return render(request,'logout.html',{})


def user_delete(request,id=None):
    instance = get_object_or_404(Users,id=id)
    instance.delete()
    return redirect('index')
