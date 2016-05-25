from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User
from bananasorter.models import Classifier, Category
from bananasorter.forms import ClassifierForm, CategoryForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import UserSerializer, ClassifierSerializer, CategorySerializer


class ClassifierViewSet(viewsets.ModelViewSet):
    queryset = Classifier.objects.all()
    serializer_class = ClassifierSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('-classifier')
    serializer_class = CategorySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-last_login')
    serializer_class = UserSerializer


def index(request):
    context = {}
    classifier_list = Classifier.objects.all().order_by('name')[:20]
    context = {'classifier_list': classifier_list}
    return render(request, 'bananasorter/index.html', context)


def detail(request, id):
    context = {}
    classifier = Classifier.objects.get(id=id)
    context['classifier'] = classifier
    context['categories'] = Category.objects.filter(classifier=classifier)

    if request.method == 'POST':
        if request.POST['action'] == 'Classify this!':
            new_text = request.POST['new_text']
            prediction = classifier.predict(new_text)
            context['new_text'] = new_text
            context['prediction'] = prediction[0]

        elif request.POST['action'] == 'Submit':
            form = CategoryForm(request.POST)
            print(form, "got to submit")
            if form.is_valid():
                print(form, "is valid")
                cat = form.save(commit=False)
                cat.classifier = classifier
                cat.save()

        elif request.POST['action'] == 'DELETE':
            print('delete it')
            classifier.delete()
            return HttpResponseRedirect('/profile/')

    context['classifier_form'] = ClassifierForm()
    context['category_form'] = CategoryForm()
    return render(request, 'bananasorter/detail.html', context)


def profile(request):
    context = {}
    context['user'] = request.user
    context['user_class_list'] = Classifier.objects.filter(owner=request.user)

    if request.method == 'POST':
        if request.POST['new_classifier']:
            form = ClassifierForm(request.POST)
            print(form, "got to submit")
            if form.is_valid():
                print(form, "is valid")
                clssf = form.save(commit=False)
                clssf.owner = request.user
                clssf.save()

    context['classifier_form'] = ClassifierForm()
    return render(request, 'bananasorter/profile.html', context)
