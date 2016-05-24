from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User
from bananasorter.models import Classifier, Category
from bananasorter.forms import ClassifierForm, CategoryForm

def index(request):
    return render(request, 'bananasorter/index.html')

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


def profile(request):
    return render(request, 'bananasorter/profile.html')
