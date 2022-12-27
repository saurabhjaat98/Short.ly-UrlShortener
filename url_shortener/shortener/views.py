from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from .models import Url
import uuid
from .forms import *


# Create your views here.


def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        Url(link=link, uuid=uid).save()
        data = Url.objects.all()
        return render(request, './home.html', {"data": data})
    else:
        data = Url.objects.all()
        return render(request, './home.html', {'data': data})


def GoToMainUrl(request, pk):
    data = Url.objects.get(uuid=pk)
    return redirect(data.link)


def deleteUrl(request, pk):
    data = Url.objects.get(uuid=pk)
    data.delete()
    return redirect('create')


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        user = request.POST['username']
        print(user)
        print(MyUser.objects.filter(username=user))
        if pass1 == pass2:
            if not MyUser.objects.filter(username=user):
                if form.is_valid():
                    form.save()
                    messages.success(request, 'you are signup successfully')
                    return redirect('LogIn')
                else:
                    messages.error(request, 'password should be strong or must be different form username')
            else:
                messages.error(request, f'This username <{user}> already exist,You need to logIn')
        else:
            messages.error(request, 'password fields do not match')
    form = UserForm()
    return render(request, './signup.html', {'form': form})

# for check query set is empty or not

# if not MyUser.objects.filter(username=user):
#     The Queryset is empty ...
# else:
#     The Queryset has results ..





# def login(request):
#     if request.method == 'POST':
#         un = request.POST.get('username')
#         ps = request.POST.get('password')
#         Userdata = User.objects.all()
#         print(Userdata)
#         for data in Userdata:
#             print(data)
#             if un == data:
#                 if ps == request.objects.get(password=un):
#                     return HttpResponse('login successful')
#                 else:
#                     return HttpResponse('password wrong')
#             else:
#                 return HttpResponse('you do not have an account')
#     form = LoginForm(request.POST)
#     return render(request, './login.html',{'form':form})
