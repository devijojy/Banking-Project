from django.contrib import auth, messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from .forms import PersonCreationForm
from .models import Person, Branch


# Create your views here.
def home(request):
    return render(request,'home.html')
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('page')
        else:
            # messages.info(request, "invalid credentials")
            return redirect('login')

    return render(request,"login.html")

def register(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('login')

        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")

def page(request):
    return render(request,'page.html')
def form(request):

        form = PersonCreationForm()
        if request.method == 'POST':
            form = PersonCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('form')
        return render(request, 'form.html', {'form': form})

def load_branches(request):
    district_id = request.GET.get('district_id')
    branches = Branch.objects.filter(district_id=district_id).all()
    return render(request, 'branch_dropdown_list_options.html', {'branches': branches})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

def submit(request):
    return render(request,'submit.html')