from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def loginView(request):
    if request.method=='POST':
        u=request.POST.get('un')
        p=request.POST.get('pw')
        user=authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            return redirect ('add_dept')
        else:
            messages.error(request,'Invalid credentials')
    template_name='LoginApp/login.html'
    context={}
    return render(request,template_name,context)

def registerView(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    template_name = 'LoginApp/register.html'
    context = {'form':form }
    return render(request, template_name, context)

def logoutView(request):
    logout(request)
    return redirect('login')


