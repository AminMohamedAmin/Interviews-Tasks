from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
from . import models
from . import forms
from django.http import FileResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


def inlog(request):
    return render(request, 'login.html', {})


# def uploadfiles(request):
#     data = models.file.objects.all()
#     user=models.file()
#     form=forms.file_form(request.POST,request.FILES)
#     if form.is_valid():
#         user.name=form.cleaned_data['name']
#         user.file = form.cleaned_data['file']
#         user.save()
#         return HttpResponseRedirect('/')
#     return render(request, 'index.html', {'form':form, 'data':data})


# def read_file(request, id):
#     d= models.file.objects.get(id=id)
#     return FileResponse(open(d.file.path, 'rb'))


def saveregisteree(request):
    try:
        if User.objects.filter(email=request.POST['eemail']):
            messages.error(request, 'email is existed, try Login')
            return render(request, 'login.html', {})
        else:
            user = User.objects.create_user(request.POST['uusername'], request.POST['eemail'], request.POST['ppassword'])
            user.first_name = request.POST['ffirst_name']
            user.last_name = request.POST['llast_name']
            user.save()
            messages.success(request, 'Successfuly Signed')
            return render(request, 'login.html',{})
    except:
        messages.error(request, 'User is exist, try Login')
        return render(request, 'login.html',{})


def saveinlogee(request):
    form = forms.file_form(request.POST, request.FILES)
    if models.file.objects.filter(username=request.POST['usernamee']).exists() == True:
        userr = request.POST['usernamee']
        data = models.file.objects.get(username=userr)
        return render(request, 'employee2.html', {'form':form, 'u':userr, 'd':data})
    else:
        u=request.POST['usernamee']
        p= request.POST['passwordd']
        result=authenticate(username=u,password=p)
        if result is not None:
            login(request,result)
            return render(request, 'emloyee.html', {'uu':u, 'form':form})
        else:
            messages.error(request, 'User is not exist')
            return render(request, 'login.html', {})


def ee(request):
        user = models.file()
        form = forms.file_form(request.POST, request.FILES)
        if form.is_valid():
            user.username = request.POST['UserName']
            user.job = request.POST['JobTitle']
            user.level = request.POST['Level']
            user.file = form.cleaned_data['file']
            user.save()
            messages.success(request, 'Successfuly Saved')
            return render(request, 'employee2.html',{'form':form})
        messages.error(request, 'Failed Saved')
        return render(request, 'emloyee.html',{'form':form})


# def read_file(request,username):
#     d = models.file.objects.get(username=username)
#     return FileResponse(open(d.file.path, 'rb'))


def saveupdate(request):
    form = forms.file_form(request.POST, request.FILES)
    if form.is_valid():
        us = request.POST['UserName']
        JobTitle = request.POST['JobTitle']
        Level = request.POST['Level']
        File = form.cleaned_data['file']

        new = models.file(username=us)
        new.job = JobTitle
        new.level = Level
        new.file = File
        new.save()
        return render(request, 'employee2.html',{'us':us, 'form':form})
    messages.error(request, 'form is not valid')
    return render(request, 'employee2.html', {'form': form})


#logoutee
def outlogee(request):
    logout(request)
    return HttpResponseRedirect('/')





#loginer
def saveinloger(request):
    u=request.POST['usernamee']
    p= request.POST['passwordd']
    result=authenticate(username=u,password=p)
    if result is not None:
        login(request,result)
        return HttpResponseRedirect('/er')
    else:
        return HttpResponse('user is not exist')


def er(request):
    return render(request, 'employer.html', {})


#logouter
def outloger(request):
    logout(request)
    return HttpResponseRedirect('/')


#registerer
def saveregisterer(request):
    try:
        user=User.objects.create_user(request.POST['uusername'],request.POST['eemail'],request.POST['ppassword'])
        user.first_name=request.POST['ffirst_name']
        user.last_name = request.POST['llast_name']
        user.save()
        messages.success(request, 'Successfuly Signed')
        return HttpResponseRedirect('/')
    except:
        return HttpResponse('user is exist')