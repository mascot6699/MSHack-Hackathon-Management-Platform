from django.shortcuts import render
from django.views import generic

from .forms import AmbassadorInfoForm


class HomePage(generic.TemplateView):
    template_name = "home.html"


class Chat(generic.TemplateView):
    template_name = "index.html"

# Deprecated
# class ApplyPage(generic.TemplateView):
#     template_name = "apply.html"
#

def apply_new(request):
    form = AmbassadorInfoForm()
    return render(request, 'apply.html', {'form': form})


class AboutPage(generic.TemplateView):
    template_name = "about.html"