from django import forms
from .models import Post, Tag

class createPostForm(forms.ModelForm):
	# summary	= forms.CharField(label='A short summary', required=False, widget=forms.Textarea(attrs={'class':'form-control'}))
	# summary	= forms.CharField(label='A short summary', required=False)
	class Meta:
		model = Post
		fields = ('title',"body",'tag','summary','cover_image_url')
		tag = forms.ModelChoiceField(queryset=Tag.objects.all())
		widgets = {
			'title'		: forms.TextInput(attrs={'class':'form-control'}),
			'body'		: forms.Textarea(attrs={'class':'form-control'}),
			'tag'		: forms.SelectMultiple(attrs={'class':'form-control'}),
			'summary'	: forms.TextInput(attrs={'class':'form-control'}),
			'cover_image_url' : forms.URLInput(),
		}


class editPostForm(forms.ModelForm):
	# summary	= forms.CharField(label='A short summary', required=False, widget=forms.Textarea(attrs={'class':'form-control'}))
	# summary	= forms.CharField(label='A short summary', required=False)
	class Meta:
		model = Post		
		fields = ('title',"body",'tag','summary','cover_image_url')
		tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())
		widgets = {
			'title'		: forms.TextInput(attrs={'class':'form-control'}),
			'body'		: forms.Textarea(attrs={'class':'form-control'}),
			'tag'		: forms.SelectMultiple(attrs={'class':'form-control'}),
			'summary'	: forms.Textarea(attrs={'class':'form-control'}),
			'cover_image_url' : forms.URLInput(),
		}