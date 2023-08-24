from django.db import models
from django.contrib.auth.models import User

import os
import random
from django.conf import settings
from django.templatetags.static import static

from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils.text import slugify

class Tag(models.Model):
	name = models.CharField(max_length=30)
	def __str__(self):
		return self.name

	def tagCount(self):
		'''Returns total like counts on Post model
		Another method as below without adding tagCount() function to class.
		Use annotate in views.py to order tags list by post count.
		allTags = Tag.objects.all().annotate(tag_posts_count=Count('post')).order_by('-tag_posts_count')
		'''
		return Post.objects.filter(tag__name__icontains=self.name).count()


class Post(models.Model):
	title = models.CharField(max_length=200)	
	slug = models.SlugField(max_length=200, blank=True, null=True, unique=True)
	author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
	summary = models.CharField(max_length=500)
	body = RichTextField(blank=True,null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	tag = models.ManyToManyField(Tag, blank=True)
	likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
	is_approved = models.BooleanField(default=False)
	cover_image_url = models.URLField(null=True, blank=True)
	cover_image_file = models.CharField(max_length=200, blank=True, null=True)
	

	def __str__(self):
		return self.title

	# def get_absolute_url(self):
	# 	return reverse('post-detail',kwargs={'pk' : self.pk})  
	
	def get_absolute_url(self):
		return reverse('post_detail',kwargs={'slug' : self.slug}) 

	def LikeCount(self):
		'''Returns total like counts on Post model'''
		return self.likes.count()
	
	def _get_unique_slug(self):
		'''generate url slug from Blog post title'''
		self.slug = slugify(self.title[:50])
		unique_slug = self.slug
		num = 1
		while Post.objects.filter(slug=unique_slug).exists():
			unique_slug = f'{self.slug}-{num}'
			num += 1
		return unique_slug

	def random_cover_image(self):
		'''select random image as cover_image for Post Model Object, if no cover image url is provided'''
		images_dir = os.path.join(settings.STATIC_ROOT, 'images', 'random')
		images = [f for f in os.listdir(images_dir) if os.path.isfile(os.path.join(images_dir,f))]
		random_image = random.choice(images)
		 # Generate the URL for the randomly chosen image
		return static('images/random/' + random_image)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = self._get_unique_slug()

		#if cover_image_url is null & cover_image_file is null, then store a random image as cover
		if not self.cover_image_url and not self.cover_image_file:
			self.cover_image_file = self.random_cover_image()	
			print(f'self.cover_image_file = {self.cover_image_file}')	
		super().save(*args, **kwargs)