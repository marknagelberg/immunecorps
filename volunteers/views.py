from django.shortcuts import render, redirect


def home_page(request):
    return render(request, 'volunteers/home.html')


def join_immunecorps(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        return redirect('views.check_email')
    return render(request, 'volunteers/join-immunecorps.html')


def check_email(request):
    return render(request, 'volunteers/check-email.html')
