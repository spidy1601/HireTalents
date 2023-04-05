from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.http import HttpResponse
from djf_surveys.views import SurveyFormView
from django.contrib import messages
from djf_surveys.models import Survey, UserAnswer
from django.utils.translation import gettext, gettext_lazy as _  
from django.template.loader import get_template
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from djf_surveys.mixin import ContextTitleMixin
from djf_surveys.forms import CreateSurveyForm
from django.views.generic import DetailView 
from .forms import DeveloperForm
from .logics import *
from django.views import View
from .models import DeveloperImage

def home(request):
    client="clients-requirements"
    employee = "create-employee"
    return render(request,'home.html',{'client':client,'employee':employee})

class CreateSurveyFormView(ContextTitleMixin, SurveyFormView):
    template_name = 'master.html'
    model = Survey
    form_class = CreateSurveyForm
    success_url = reverse_lazy("home")
    title_page = _("Add Survey")


    def dispatch(self, request, *args, **kwargs):
        survey = self.get_object()
        # handle if survey can_anonymous_user
        if not request.user.is_authenticated and not survey.can_anonymous_user:
            messages.warning(request, gettext("Sorry, you must be logged in to fill out the survey."))
            return redirect("home")

        # handle if user have answer survey
        if request.user.is_authenticated and not survey.duplicate_entry and \
                UserAnswer.objects.filter(survey=survey, user=request.user).exists():
            messages.warning(request, gettext("You have submitted out this survey."))
            return redirect("home")
        return super().dispatch(request, *args, **kwargs)
    def post(self,request,*args,**kwargs):
        # print(request.FILES['image'])
        image=''
        if image:
            image = request.FILES['image']
            my_model = DeveloperImage(developer_image=image)
            my_model.save()
        return super().post(self,request,*args,**kwargs)

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(survey=self.get_object(), user=self.request.user, **self.get_form_kwargs())

    def get_title_page(self):
        return self.get_object().name

    def get_sub_title_page(self):
        return self.get_object().description

def display(request):
    client_skills = Answer.objects.filter(question_id=5).values_list(Lower('value'),flat=True)
    client_skills= client_skills[len(client_skills)-1].split(",")
    nums = search_dev(client_skills)
    if request.method =="POST":
        print(request.POST)
    all_dev_details=get_dev_details(nums)
    return render(request,'display.html',{'all_dev_details':all_dev_details})

def searching(request):
    return render(request,'searching.html') 