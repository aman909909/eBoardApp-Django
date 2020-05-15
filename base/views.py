from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from .models import board, nlist, card, cardComment
from .forms import cardForm


def home(request):
    return render(request, 'base/home.html')


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home_page')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home_page')
        else:
            messages.info(request,"Username/Password invalid")
            return render(request,'base/login.html')
    return render(request,'base/login.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('home_page')
    if request.method == "POST":
        name = request.POST['username']
        email = request.POST['email']
        pwd1 = request.POST['password1']
        pwd2 = request.POST['password2']
        try:
            user=User.objects.get(username=name)
        except:
            if pwd1 != pwd2:
              messages.info(request,"Password don't match")
              return render(request,'base/signup.html')
            if len(pwd1)<8:
                messages.info(request,"Password is too short")
                return render(request,'base/signup.html')
            
            uss = User.objects.get(email = email)
            if uss is None:

                 us = User()

                 us.username = name
                 us.email = email
                 us.set_password(pwd1)
                 us.save()
            
            else:
                  messages.success(request,"Email already exists.")
                  return redirect('signup_page')

            #p=UserProfile()
            #user = User.objects.get(username=name)
            #p.user = user
            #p.occupation = request.POST['occupation'] 
            #p.phone = request.POST['phone']
            #p.save()

            messages.success(request,"Signed up successfully")
            return redirect('login_page')
        else :
            messages.info(request,"Username already exists")
            return render(request,'base/signup.html')
    return render(request,'base/signup.html')


def logoutUser(request):
    logout(request)
    return render(request,'base/home.html')

@login_required(login_url='login_page')
def newBoard(request):
    if request.method=="POST":
        b = board()
        
        b.user = request.user
        b.name = request.POST['name']
        b.description = request.POST['description']
        b.author = request.user
        b.save()
        return redirect('dashboard_page')

    return render(request,'base/newboard.html')

@login_required(login_url='login_page')
def dashboard(request):

    b = board.objects.all().filter(user=request.user).order_by('-id')
    return render(request,'base/dashboard.html',{
        'b':b
    })
@login_required(login_url='login_page')
def newList(request, z):
    if request.method=="POST":
        z=int(z)
        b = board.objects.all().filter(id=z)
        n = nlist()
        n.list_name = request.POST['name']
        n.parent = b[0]
        n.save()
        l = nlist.objects.all().filter(parent = z)
        c = card.objects.all()

        return redirect('board_page', z=z)
        return render(request,'base/board.html',{
            'l':l,
            'val':z,
            'c':c
        })
    return HttpResponse('Wrong HTTP method')



@login_required(login_url='login_page')
def boardDisplay(request, z):
    l = nlist.objects.all().filter(parent = z)
    c = card.objects.all()
    
    context={
        'l':l,
        'val':z,
        'c':c
    }
    return render(request, 'base/board.html',context)
    
@login_required(login_url='login_page')
def addCard(request,z):
    if request.method=="POST":
        c = card()
        c.title = request.POST['name']
        c.dad = z
        
        c.save()
        fi = nlist.objects.all().filter(pk=z)
        nex = fi[0]
        boarp = nex.parent
        sen = boarp.pk
        ca = card.objects.all()
        la = nlist.objects.all().filter(parent = sen)
        print(la)
        context = {
            
            'val':sen,
            'c':ca,
            'l':la
        }
        
        return redirect('board_page',z=sen)

@login_required(login_url='login_page')
def dellist(request, z):
    
    ll = nlist.objects.all().filter(pk=z)
    f =ll[0].parent
    print(f.id)
    z=f.id
    ll.delete()

    return redirect('board_page',z=z)

def cardDetail(request, z):

    if request.method=='POST':
        form = cardForm(request.POST)
        if form.is_valid():
             ca = card.objects.all().filter(id = z)
             ca = ca[0]
             new = form.cleaned_data['des']
             print(new)
             if new is not '':
                ca.des = new
             ca.deadline = form.cleaned_data['deadline']
             ca.save()


    ca = card.objects.all().filter(id = z)
    form = cardForm()
    cmnt = cardComment.objects.all().filter(owner = z)
    return render(request, 'base/carddetail.html',{
        'ca':ca,
        'form':form,
        'cmnt':cmnt
    })

def cardcmnt(request, z):
    if request.method == 'POST':
        ca = cardComment()
        fi = card.objects.all().filter(id=z)
        fi=fi[0]
        ca.owner = fi
        ca.comment = request.POST['ct']
        ca.save()
        return redirect('card_page', z=z)


def cardDelete(request, z):
    ca = card.objects.all().filter(id=z)
    ca.delete()
    return redirect('home_page')


