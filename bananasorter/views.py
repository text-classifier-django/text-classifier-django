from django.shortcuts import render
from .models import User, Classifier, Category

def index(request):

    context = {}
    calssifier_list = Classifier.objects.all().order_by('name')[:20]

    context = {'classifier_list' : calssifier_list}

    return render(request, 'bananasorter/index.html', context)

# def detail(request):
#     return render('bananasorter/detail.html')
#
#
# def profile(request):
#     return render('bananasorter/profile.html')
