from django.shortcuts import render
from django.http import HttpResponse
from babbel.models import BabbelCode
from busuu.models import Course
from duolingo.models import Duolingo
from memrise.models import Memrise
from django.contrib.auth.decorators import login_required
@login_required
def index(request):
    return render(request,'index.html')
@login_required
def babbel(request):
    language = BabbelCode.objects.all()
    return render(request, "babbel.html" ,{'BabbelCode':language})
@login_required
def busuu(request):
    learning = Course.objects.all()
    return render(request, "busuu.html" ,{'Course': learning})
@login_required
def duolingo(request):
    application = Duolingo.objects.all()
    return render(request, "duolingo.html" ,{'Duolingo': application})
@login_required
def memrise(request):
    project = Memrise.objects.all()
    return render(request, "memrise.html" ,{'Memrise': project})
@login_required
def forms(request):
    # Your view logic here
    return render(request, 'Duolingo_form.html')