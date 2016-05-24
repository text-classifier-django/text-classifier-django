from django.shortcuts import render
from django.contrib.auth.models import User
from bananasorter.models import Classifier, Category
from bananasorter.forms import ClassifierForm, CategoryForm

def index(request):
    return render('bananasorter/index.html')

def detail(request, id):
    context = {}
    classifier = Classifier.objects.get(id=id)
    context['classifier'] = classifier
    context['categories'] = Category.objects.filter(classifier=classifier)
    context['classifier_form'] = ClassifierForm()
    context['category_form'] = CategoryForm()
    return render(request, 'bananasorter/detail.html', context)


def profile(request):
    return render('bananasorter/profile.html')
