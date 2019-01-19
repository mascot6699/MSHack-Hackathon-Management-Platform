from django.views import generic


class HomePage(generic.TemplateView):
    template_name = "home.html"


class Chat(generic.TemplateView):
    template_name = "index.html"


class ApplyPage(generic.TemplateView):
    template_name = "apply.html"

class AboutPage(generic.TemplateView):
    template_name = "about.html"