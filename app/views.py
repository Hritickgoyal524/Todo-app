from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate , login as loginuser,logout
from django.contrib.auth.decorators import login_required
from app.forms import TodoForm
from app.models import TODO

# Create your views here.
@login_required(login_url="login")
def home(request):
    if request.user.is_authenticated:
       user=request.user
       form=TodoForm()
       todo=TODO.objects.filter(user=user).order_by('priority')
       context={
       'form':form,
       "todos":todo
        }
       return render(request,'index.html',context)
def login(request):
    if request.method=="GET":
       form=AuthenticationForm()
       context={
        'form':form
       }
       return render(request,'login.html',context)
    else:
       form=AuthenticationForm(data=request.POST)
      
       context={
        'form':form
       }
       if form.is_valid():
          print("jfjafaftgagasgasgasgagasg")
          username=form.cleaned_data.get("username")
          password=form.cleaned_data.get("password")
          user=authenticate(username=username,password=password)
          print("userfafag")
          if user is not None:
            loginuser(request,user)
            return redirect("home")
       else:
           return render(request,'login.html',context)
def signup(request):
   
    if request.method=="GET":
       form=UserCreationForm()
       context={
        'form':form
       }
       return render(request,'signup.html',context)
    else:
        form=UserCreationForm(request.POST)
        context={
        'form':form
        }
        if form.is_valid():
             user=form.save()
             if user is not None:
                return redirect('login')
        else:
           return render(request,'signup.html',context) 
@login_required(login_url="login")           
def app_todo(request):
    if request.user.is_authenticated:
       user=request.user
       form=TodoForm(request.POST)
       context={
        'form':form
       }
       if form.is_valid():
          todo=form.save(commit=False)
          todo.user=user
          todo.save()
          return redirect("home")
       else:
          return render(request,'index.html',context)  
def signout(request):
    print("print")
    logout(request)
    return redirect('login')    
def delete_todo(request,id):
    TODO.objects.get(pk=id).delete()
    return redirect("home")
def change_todo(request,id,status):
    todo=TODO.objects.get(pk=id)
    todo.status=status
    todo.save()
    return redirect("home")
