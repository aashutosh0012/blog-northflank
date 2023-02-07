from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from accounts.forms import *

#@login_required : requires user to login before executing functions based views, un-authenticated users will be redirected to login
#Add in settings.py  LOGIN_URL='login/', or in view function @login_required(login_url='login/') 
from django.contrib.auth.decorators import login_required 

#LoginRequiredMixin is class based which requires authentication and un-authenticated users will be redirected to login.
#UserPassesTestMixin tests a function for any custom check, before running the class based view 
#Add in settings.py 	 LOGIN_URL='login/', or in view function @login_required(login_url='login/') 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class  userRegistrationView(generic.CreateView):
	#form_class = UserCreationForm #django generic UserCreationForm
	form_class = userRegisterForm
	template_name = 'templates/registration/register.html'
	success_url = reverse_lazy('login')

#Django's default generic.UpdateView & UserChangeForm
# class editProfileView(generic.UpdateView):
# 	form_class = UserChangeForm
# 	template_name = 'registration/editProfile.html'
# 	success_url = 'blog-home'
# 	def get_object(self):
# 		#returns self logged in user data to the Update Form
# 		return self.request.user

#Custom Form Class editProfileView
class editProfileView(LoginRequiredMixin, generic.UpdateView):
	form_class = editProfileForm
	template_name = 'registration/editProfile.html'
	success_url = reverse_lazy('home')
	def get_object(self):
		#returns self logged in user data to the Update Form
		return self.request.user

# class passwordResetView():
# 	