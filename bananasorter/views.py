from django.shortcuts import render

def index(request):
    return render('bananasorter/index.html')

def detail(request):
    return render('bananasorter/detail.html')


def profile(request):
    return render('bananasorter/profile.html')
