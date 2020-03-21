from django.shortcuts import render


def home_page(request):
    return render(request, 'volunteers/home.html')


def join_immunecorps(request):
    return render(request, 'volunteers/join-immunecorps.html')


def check_email(request):
    return render(request, 'volunteers/check-email.html')
