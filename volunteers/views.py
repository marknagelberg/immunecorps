from django.shortcuts import render, redirect
from volunteers.models import Volunteer


def home_page(request):
    return render(request, 'volunteers/home.html')


def join_immunecorps(request):
    if request.method == 'POST':
        new_volunteer_email = request.POST['email']
        Volunteer.objects.create(email=new_volunteer_email)
        return redirect('/volunteers/check-email')
    return render(request, 'volunteers/join-immunecorps.html')


def new_volunteer(request):
    volunteer = Volunteer.objects.create(email=request.POST['email'])
    return redirect(f'/volunteers/{volunteer.id}/')


def check_email(request):
    return render(request, 'volunteers/check-email.html')


def vlogin_immunecorps(request):
    if request.method == 'POST':
        volunteer_email = request.POST['email']
        volunteer = Volunteer.objects.get(email=volunteer_email)
        return redirect(f'/volunteers/{volunteer.id}/')
    return render(request, 'volunteers/login.html')


def volunteer_dashboard(request, volunteer_id):
    return render(request, 'volunteers/dashboard.html')

