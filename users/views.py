from django.shortcuts import render
from django.http import Http404
from users.models import Users
from django.shortcuts import redirect
from datetime import datetime
# Create your views here.


def welcome(request):
    return render(request, "welcome.html")

def index(request):
    users = Users.objects.all()

    return render(request, "index.html", {'users': users,})

def add(request):
    if (request.method == "POST"):
        saved = False

        user = Users(name=request.POST['name'],email=request.POST['email'])

        user.save()

        id = user.id
        if (id is not None):
            saved = True
            return redirect("view",id=id)

    return render(request, "add.html")

def view(request,id):
    try:
        user = Users.objects.get(id=id)
    except:
        raise Http404("Record not found")

    return render(request,"view.html",{"user":user})

def edit(request,id):
    try:
        user = Users.objects.get(id=id)
    except:
        raise Http404("Record not found")

    if (request.method == "POST"):
        saved = False

        user.name = request.POST['name']
        user.email = request.POST['email']
        user.save()

        name = user.name
        email = user.email
        if (name == request.POST['name'] and email == request.POST['email']):
            saved = True
            return redirect("view",id=id)

    return render(request,"edit.html",{"user":user})
