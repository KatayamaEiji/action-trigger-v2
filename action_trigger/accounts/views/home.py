from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginRequiredMixin, TemplateView):#「LoginRequiredMixin → TemplateView」この順番で記述しないとログイン必須機能が表れないので注意！！
    template_name = 'accounts/home.html'
    login_url = '/login/'