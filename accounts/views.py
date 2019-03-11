from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, TemplateView, CreateView, UpdateView
from django.contrib.auth import logout
from .forms import RegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from django.contrib.messages.views import SuccessMessageMixin


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')


class RegisterView(SuccessMessageMixin, CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_message = "Account Created Successfully"
    success_url = reverse_lazy('login')


class ProfileView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = RegisterForm
    template_name = 'registration/profile.html'
    queryset = User.objects.all()
    success_url = reverse_lazy('my_posts')
    success_message = "Profile Updated Successfully"


class ImageUpdateView(LoginRequiredMixin, TemplateView):
    template_name = 'registration/profile_picture.html'

    def post(self, request, *args, **kwargs):
        img = request.FILES.get('image')
        user = get_object_or_404(User, username=request.user.username)
        user.profile.image = img
        user.save()
        return redirect('profile', request.user.id)
