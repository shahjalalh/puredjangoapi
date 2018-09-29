from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.


class UserProfileView(TemplateView):
    template_name = 'userprofiles/userprofile.html'
