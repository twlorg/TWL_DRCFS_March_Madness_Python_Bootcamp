from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# import todo form and models

from .forms import TodoForm, NewUserForm
from .models import Todo
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

@login_required(login_url="/login")   
def index(request):

    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form=TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    
    form=TodoForm()

    page = {
        'forms':form,
        'list':item_list,
        'title':'DRCFS & TWL Bootcamp'
    }

    return render(request, 'todoapp/todoapp.html', page)

@login_required(login_url="/login") 
def remove(request, item_id):
   
    item=Todo.objects.get(id=item_id)  # we are accessing specific item in datebase
    item.delete()
    messages.info(request, "item removed !! ")
    return redirect("todo")




# let's make login system

# for singup feature 

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successfull!!")
            return redirect("login")
        messages.error(request, "Registration unsuccessfull!! Invalid information")

    form = NewUserForm()
    return render(request=request, template_name="loginsystem/register.html", context={"register_form":form})
        

# for login feature


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f"You are loggedin {username} ")
                return redirect("todo")
            else:
                messages.error(request, "Your login unsuccessfull!!")
        else:
            messages.error(request, "Your invalid logins")

    form = AuthenticationForm()

    return render(request=request, template_name="loginsystem/login.html", context={"login_form":form})

            



        