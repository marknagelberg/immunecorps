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


def check_email(request):
    return render(request, 'volunteers/check-email.html')
