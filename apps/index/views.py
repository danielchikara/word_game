from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.contrib.auth import login
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .forms import CustomUserCreationForm
from . models import *

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('index')
    template_name = 'registration/signup.html'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request,self.object)
        return response
    
class Index(TemplateView):
    template_name = "index/home.html"
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        questions = Word.objects.all().order_by('?')
        context['questions'] = questions
        music_questions = SongsWord.objects.all().order_by('?').first()
        context['music_questions'] = music_questions
        return context

# Create your views here.