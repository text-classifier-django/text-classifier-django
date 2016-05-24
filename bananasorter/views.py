from django.shortcuts import render

def index(request):
    return render('bananasorter/index.html')

def detail(request, id):
    context = {}
    context['classifier'] = Classifier.objects.get(id=id)
    return render(request, 'bananasorter/detail.html', context)


def profile(request):
    return render('bananasorter/profile.html')
