from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.hashers import check_password, make_password
from . models import *

# Create your views here.


def index(request):
    return render(request, 'hello.html')


def log_in(request):
    return render(request, 'login.html')


def logout(request):
    request.session.clear()
    return redirect('hello')


def register(request):
    return render(request, 'register.html')


def Registration(request):
    if request.method == 'POST':
        name = request.POST.get('email')
        pwd = request.POST.get('pass')

        s = registration(
            user_name=name,
            password=make_password(pwd)

        )
        s.save()
        return redirect('log_in')


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        Password = request.POST.get('pass')
        try:
            fetch_obj = registration.objects.get(user_name=email)
            if check_password(Password, fetch_obj.password):
                request.session['name'] = fetch_obj.user_name
                return render(request, 'login2.html')

            else:
                return HttpResponse("please insert a valid password")
        except:
            return HttpResponse("please insert correct email")


def inc(request):
    return render(request, 'incidents.html ')


def Incident(request):
    if request.method == 'POST':
        Location = request.POST.get('location'),
        Department = request.POST.get('idepart'),
        Date = request.POST.get('date'),
        Time = request.POST.get('time'),
        Incident_location = request.POST.get('ilocation'),
        Severity = request.POST.get('severity'),
        Suspected_cause = request.POST.get('cause'),
        Action = request.POST.get('action'),
        Sub_incident = request.POST.get('check'),
        User = request.POST.get('user')

        a = incident(
            location=Location,
            department=Department,
            date=Date,
            time=Time,
            incident_location=Incident_location,
            severity=Severity,
            suspected_cause=Suspected_cause,
            action=Action,
            sub_incident=Sub_incident,
            user=User,
        )
        a.save()
        return redirect('hello')
