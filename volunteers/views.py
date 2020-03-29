from django.shortcuts import render, redirect
from volunteers.models import Volunteer


def home_page(request):
    return render(request, 'volunteers/home.html')


def join_immunecorps(request):
    if request.method == 'POST':
        new_volunteer_email = request.POST['email']
        Volunteer.objects.create(email=new_volunteer_email)
        return redirect('/check-email')
    return render(request, 'volunteers/join-immunecorps.html')


def new_volunteer(request):
    Volunteer.objects.create(email=request.POST['email'])
    return redirect('/volunteers/the-only-volunteer-in-the-world/')


def check_email(request):
    return render(request, 'volunteers/check-email.html')


def vlogin_immunecorps(request):
    if request.method == 'POST':
        volunteer_email = request.POST['email']
        return redirect('/volunteers/the-only-volunteer-in-the-world/')
    return render(request, 'volunteers/login.html')


def volunteer_dashboard(request):
    return render(request, 'volunteers/dashboard.html')

