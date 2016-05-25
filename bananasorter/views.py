from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User
from bananasorter.models import Classifier, Category, User
from bananasorter.forms import ClassifierForm, CategoryForm
from django.shortcuts import render



def index(request):

    context = {}
    calssifier_list = Classifier.objects.all().order_by('name')[:20]
    context = {'classifier_list' : calssifier_list}
    return render(request, 'bananasorter/index.html', context)



def detail(request, id):
    context = {}
    classifier = Classifier.objects.get(id=id)
    context['classifier'] = classifier
    context['categories'] = Category.objects.filter(classifier=classifier)

    if request.method == 'POST':
        if request.POST['name'] == 'Classify this!':
            new_text = request.POST['new_text']
            prediction = classifier.predict(new_text)
            context['new_text'] = new_text
            context['prediction'] = prediction[0]

        elif request.POST['new_category']:
            form = CategoryForm(request.POST)
            print(form, "got to submit")
            if form.is_valid():
                print(form, "is valid")
                cat = form.save(commit=False)
                cat.classifier = classifier
                cat.save()

        elif request.POST['delete']:
            print('delete it')
            classifier.delete()
            return HttpResponseRedirect('/profile/')

    context['classifier_form'] = ClassifierForm()
    context['category_form'] = CategoryForm()
    return render(request, 'bananasorter/detail.html', context)

def detail(request):
    return render('bananasorter/detail.html')


def profile(request):
    context = {}
    context['user'] = request.user
    context['classifier_list'] = Classifier.objects.filter(owner=request.user)

    if request.method == 'POST':
        if request.POST['new_classifier']:
            form = ClassifierForm(request.POST)
            print(form, "got to submit")
            if form.is_valid():
                print(form, "is valid")
                classifier_list = form.save(commit=False)
                classifier_list.save()

    context['classifier_form'] = ClassifierForm()
    return render(request, 'bananasorter/profile.html')
