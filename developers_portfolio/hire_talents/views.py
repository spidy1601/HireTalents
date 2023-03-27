from django.shortcuts import redirect, render
from django.urls import reverse_lazy

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

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(survey=self.get_object(), user=self.request.user, **self.get_form_kwargs())

    def get_title_page(self):
        return self.get_object().name

    def get_sub_title_page(self):
        return self.get_object().description

def home(request):
    slug="clients-requirements"
    return render(request,'home.html',{'slug_text':slug})