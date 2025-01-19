from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Profile,Events,Tasks
from .forms import RegistrationForm,CreateventForm,TasksForm
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import CreateView
from django.conf import settings
from django.core.mail import send_mail
import requests
import os
from datetime import datetime
from django.forms import formset_factory






def members(request):
  myevents = Events.objects.all().values()
  template = loader.get_template('profile.html')
  context = {
    'myevents': myevents,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  mymember = Events.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def items(request):
    tasks = Tasks.objects.all()
    return render(request, 'task_list.html', {'task_list': tasks})





def registerationform(request):
    if request.method == 'POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email = request.POST.get('email')
        Profile.objects.create(firstname=firstname,lastname=lastname, email=email)
        


        return render(request,'noproblem.html')
    return render(request,'profile.html')



def createventform(request):
    if request.method == 'POST':
        date=request.POST.get('date')
        time=request.POST.get('time')
        location = request.POST.get('location')
        description = request.POST.get('description')
        email = request.POST.get('email')
        date = datetime.strptime(date, '%Y-%m-%d')
        time = datetime.strptime(time, '%H:%M:%S')

        Events.objects.create(date=date, time=time, location=location, description=description, email=email)

        return render(request, 'tasks.html')
    return render(request,'profile.html')






def tasksform(request):
    if request.method == 'POST':
        task=request.POST.get('task')
        date=request.POST.get('date')
        email=request.POST.get('email')
        date = datetime.strptime(date,'%Y-%m-%d')

        Tasks.objects.create(task=task,date=date,email=email)
        return render(request, 'noproblem.html')
    return render(request,'profile.html')



