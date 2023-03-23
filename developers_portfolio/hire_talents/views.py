from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import OptionForm
from .models import Question,Option

from djf_surveys.views import CreateSurveyFormView
from django.contrib import messages
from djf_surveys.models import Survey, UserAnswer
from django.utils.translation import gettext, gettext_lazy as _  

# Create your views here.

class CreateSurveyFormViewUpdated(CreateSurveyFormView):
    success_url = reverse_lazy("index")
    def __init__(self):
        print("###INSIDE")

    def dispatch(self, request, *args, **kwargs):
        survey = self.get_object()
        # handle if survey can_anonymous_user
        if not request.user.is_authenticated and not survey.can_anonymous_user:
            messages.warning(request, gettext("Sorry, you must be logged in to fill out the survey."))
            return redirect("index")

        # handle if user have answer survey
        if request.user.is_authenticated and not survey.duplicate_entry and \
                UserAnswer.objects.filter(survey=survey, user=request.user).exists():
            messages.warning(request, gettext("You have submitted out this survey."))
            return redirect("index")
        return super(CreateSurveyFormView,self).dispatch(request, *args, **kwargs)
    


def home(request):
    slug="clients-requirements"
    return render(request,'home.html',{'slug_text':slug})