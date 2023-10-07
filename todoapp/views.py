from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from todoapp.forms import TODOForm
from todoapp.models import TODO
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url = 'login')# This decorator is used for redirecting user to login page,if user is not logged in
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm()
        todos = TODO.objects.filter(user = user).order_by('priority')
        return render(request,"home.html",{"forms":form,"todos":todos})


def signup(request):
    if request.method=='GET':
        form = UserCreationForm()
        context = {"forms": form}
        return render(request,"signup.html",context)
    else:
        form = UserCreationForm(data = request.POST)
        context = {"forms": form}
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('login')    # Redirect to name = 'login' which is given in urls.py

        else:
            return render(request, "signup.html", context)

def Login(request):
    if request.method=="GET":
        form = AuthenticationForm()
        context = {"forms":form}
        return render(request, "login.html", context)
    else:
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username = username,password = password)
            if user is not None:
                login(request,user)
                return redirect('home')
        else:
            form = UserCreationForm()
            context = {"forms": form}
            return render(request, "signup.html", context)


@login_required(login_url = 'login')
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm(data = request.POST)
        if form.is_valid():
            todo = form.save(commit = False)
            todo.user = user
            todo.save()
            return redirect("home")  # This will return to home page without any errors
        else:
            return render(request, "home.html", context = {"forms": form}) # This will return to home page showing errors

@login_required(login_url = 'login')
def delete_todo(request,id):
    TODO.objects.get(pk = id).delete()
    return redirect("home")

@login_required(login_url = 'login')
def update_todo(request,id,status):
    todo = TODO.objects.get(pk = id)
    todo.status = status
    todo.save()
    return redirect("home")

def Logout(request):
    logout(request)
    return redirect("login")