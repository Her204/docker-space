from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def index(request,id):
    ls = ToDoList.objects.get(id=id)
    if ls in request.user.todolist.all():
        if request.method == "POST":
            print(request.POST)
            if request.POST.get("save"):
                for item in ls.item_set.all():
                    p = request.POST
                    if "on"==p.get("c"+str(item.id)):
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()
            elif request.POST.get("newItem"):
                txt = request.POST.get("new")
                print(txt)
                if len(txt) > 1:
                    ls.item_set.create(text=txt,complete=True)
                else:
                    print("invalid")
        return render(request,"lito_django/list.html",{"ls":ls})
    return render(request,"lito_django/view.html",{})

def home(response):
    return render(response,"lito_django/home.html",{})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()
    return render(response,"lito_django/create.html",{"form":form})

def view(response):
    return render(response,"lito_django/view.html",{})
