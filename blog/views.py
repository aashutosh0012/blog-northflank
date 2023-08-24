
from django.http import HttpResponse, HttpResponseRedirect	
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Tag, Post
from blog.forms import createPostForm, editPostForm
from django.http import JsonResponse
from django.db.models import Q 
from django.db.models import Count

#@login_required decorator: requires user to login before executing functions based views, un-authenticated users will be redirected to login
#Add in settings.py  LOGIN_URL='login/', or in view function @login_required(login_url='login/') 
from django.contrib.auth.decorators import login_required 

#LoginRequiredMixin is class based which requires authentication and un-authenticated users will be redirected to login.
#UserPassesTestMixin tests a function for any custom check, before running the class based view 
#Add in settings.py 	 LOGIN_URL='login/', or in view function @login_required(login_url='login/') 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



# def home(request):
#     return render(request,'templates/home.html')


# class post_list(ListView):
#     model = Post
#     paginate_by = 10
#     ordering = ['-updated']
#     template_name = 'templates/post_list_1.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         tag = self.kwargs.get('tag',None)
#         print(f'Tag={tag}')
#         if not tag:
#             print('True')
#             context['post_list'] = Post.objects.filter(is_approved=True).order_by('-updated')
#         else:
#             context['post_list'] = Post.objects.filter(is_approved=True).filter(tag__name__icontains=tag).order_by('-updated')
        
#         context['tags'] = Tag.objects.all()
#         return context


class post_list(ListView):
    model = Post
    paginate_by = 10
    ordering = ['-updated']
    template_name = 'templates/post_list.html'

    def get_queryset(self):
        tag = self.kwargs.get('tag',None)
        search_keyword = self.request.GET.get('q',None)
        if tag:
             return Post.objects.filter(is_approved=True).filter(tag__name__icontains=tag).order_by('-updated')
        elif search_keyword:
            return Post.objects.filter(is_approved=True).filter(
                Q(tag__name__icontains=search_keyword) | 
                Q(title__icontains = search_keyword) | 
                Q(body__icontains = search_keyword) | 
                Q(summary__icontains = search_keyword) |
                Q(author__username__icontains = search_keyword)
                ).distinct().order_by('-updated')
        
            # queryset = Post.objects.filter(is_approved=True).filter(
            #     Q(tag__name__icontains=search_keyword) | 
            #     Q(title__icontains = search_keyword) | 
            #     Q(body__icontains = search_keyword) | 
            #     Q(summary__icontains = search_keyword) |
            #     Q(author__username__icontains = search_keyword)
            #     ).distinct().order_by('-updated')
            # if not queryset.exists():
            #     message = ("No results found for the given query.")
            #     context = {'message': message}
            #     return queryset
            #     # return render(self.request, self.template_name, context)
            # return queryset
        else:
            return Post.objects.filter(is_approved=True).order_by('-updated')  
      
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all().annotate(tag_posts_count=Count('post')).order_by('-tag_posts_count')
        return context
    


class post_detail(DetailView):
    model = Post
    template_name = 'templates/post_detail.html'

    #set objectcontext name
    #context_object_name = 'post_detail'

    def get_context_data(self, **kwargs):
        context = super(post_detail, self).get_context_data(**kwargs)
        
        #set context name, default="object"
        #context["post"] = self.object

        post = get_object_or_404(Post, slug=self.kwargs['slug'])
        
        #Fetch tags of particular Post model & pass to template as list
        post_tags = list(value[1] for value in post.tag.values_list())
        context['post_tags'] = post_tags
        print(f'post_tags= {post_tags}')

        #Fetch like counts on particular Post model
        likeCounts = post.LikeCount()
        context['likes'] = likeCounts
        
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        else:
            liked = False
        context['liked'] = liked
        return context


@login_required
def like_post(request, slug):
    # slug = request.POST.get('slug')
    print(f'slug={slug}')
	# Function to like or unlike a Post.
    post = get_object_or_404(Post, slug=slug)
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post_detail', args=[str(slug)]))


class createPostView(LoginRequiredMixin, CreateView):
	model = Post
	form_class = createPostForm
	template_name = 'templates/create_post.html'
	#fields = '__all__'
	#fields = ('title','body','tag')
	
	#pass logged_in user as author to the Post Model.
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class editPostView(LoginRequiredMixin, UpdateView):
	model = Post
	template_name = 'templates/edit_post.html'
	#fields = ['title','tag','body']
	form_class = editPostForm
	# def form_valid(self, form):
	# 	tag_name = form.cleaned_data.get('tag')
	# 	tag, created = Tag.objects.get_or_create(name=tag_name)
	# 	self.object = form.save(commit=False)
	# 	self.object.tag = tag
	# 	self.object.save()
	# 	return super().form_valid(form)


class deletePostView(LoginRequiredMixin, DeleteView):
	model = Post
	template_name = 'templates/delete_post.html'
	success_url = reverse_lazy('post_list')


def like_post2(request, slug):
    # Function to like or unlike a Post.
    post = get_object_or_404(Post, slug=slug)
    likes = post.LikeCount()
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
        return HttpResponse()
    else:
        post.likes.add(request.user)
        liked = True
    print(f'like2,slug={slug}, liked={liked},likeCounts={likes}')
    #return HttpResponse({'liked':liked,'likes':likes})
    return JsonResponse({'liked':liked,'likes':likes})

