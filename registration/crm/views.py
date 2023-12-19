from django.shortcuts import render,redirect
from . forms import CreateUserForm
# Create your views here.

def homepage(request):
    return render(request, 'crm/index.html')

def register(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("my-login")
        
    context = {'registerform':form}
        
    return render(request, 'crm/register.html',context=context)





def my_login(request):
    return render(request, 'crm/my-login.html')

def dashboard(request):
    return render(request, 'crm/dashboard.html')

