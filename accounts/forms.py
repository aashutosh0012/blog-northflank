from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


class userRegisterForm(UserCreationForm):
	email = forms.EmailField(max_length=100,label='Email', required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Optional'}))
	first_name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Optional'}))
	last_name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Optional'}))
	username = forms.CharField(max_length=20, strip=True, widget=forms.TextInput(attrs={'placeholder': '20 characters','class':'form-control'}))
	#password = forms.CharField(max_length=20, strip=True, widget=forms.PasswordInput(attrs={'placeholder': 'Your wish?','class':'form-control'}))

	class Meta:
		model = User
		fields = ['username','password1', 'email', 'first_name', 'last_name']
	
	def __init__(self, *args, **kwargs):
		super(userRegisterForm, self).__init__(*args, **kwargs)
		del self.fields['password2']
		self.fields['password1'].help_text = None
		self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Your wish?','class':'form-control'})


class editProfileForm(UserChangeForm):
	username = forms.CharField(max_length=20, strip=True, widget=forms.TextInput(attrs={'placeholder': '20 characters','class':'form-control'}))
	email = forms.EmailField(max_length=100,label='Email', required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Optional'}))
	first_name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Optional'}))
	last_name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Optional'}))	
	#password = forms.CharField(max_length=20, strip=True, widget=forms.PasswordInput(attrs={'placeholder': 'Your wish?','class':'form-control'}))
	last_login = forms.DateTimeField(disabled=True)
	date_joined = forms.DateTimeField(disabled=True)
	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name', 'last_login','date_joined']
	
	# def __init__(self, *args, **kwargs):
	# 	super(userRegisterForm, self).__init__(*args, **kwargs)
	# 	del self.fields['password2']
	# 	self.fields['password1'].help_text = None
	# 	self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Your wish?','class':'form-control'})