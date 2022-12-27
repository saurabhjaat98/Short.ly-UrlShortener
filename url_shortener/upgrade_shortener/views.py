from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *


# Create your views here.


def Plans(request):
    return render(request, './upgrade_plan.html')


@login_required
def Home(request):
    # after logIn we can access user information link this
    username = request.user.username
    # here user is neither the name of a model nor name of a field in a model
    # (MyUser(User) is a main user table where user data store)
    data = LinkInfo.objects.filter(username=username)
    contex = {
        'datas': data,
        'username':username
    }
    return render(request, './main_home.html', contex)


@login_required
def UrlCreate(request):
    username = request.user.username
    print(username)
    if request.method == 'POST':
        # if request.user.is_authenticated():
        data = LinkInfo(
            username=request.user.username,
            destination=request.POST['destination'],
            title=request.POST['title'],
            domain=request.POST['domain'],
            custom_half=request.POST['custom_half']
        )
        data.save()
        return redirect('main_home')
    form = LinkForm()
    return render(request, './Link_creation_form.html', {'form': form})


def GoToDestinationUrl(request, pk):
    object = LinkInfo.objects.get(custom_half=pk)
    return redirect(object.destination)


def EditUrl(request, pk):
    if request.method == 'POST':
        data = LinkInfo.objects.get(custom_half=pk)
        form = LinkForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('main_home')

    data = LinkInfo.objects.get(custom_half=pk)
    form = LinkForm(instance=data)
    return render(request, './link_creation_form.html', {'form': form})


def DeleteUrl(request, pk):
    object = LinkInfo.objects.get(custom_half=pk)
    object.delete()
    return redirect('main_home')


@login_required
def logout_view(request):
    logout(request)
    return redirect('create')



