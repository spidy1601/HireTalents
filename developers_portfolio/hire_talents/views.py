from django.shortcuts import render
from .forms import OptionForm
from .models import Question,Option
# Create your views here.

def index(request):
    questions = Question.objects.all()
    options = Option.objects.all()
    print(request.POST)
    return render(request,'index.html',{'questions':questions,'options':options})