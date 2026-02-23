from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import ListView, DetailView, FormView, CreateView
from .models import Post

from .forms import *
# Create your views here.

# Function Based View show a template
'''
def indexView(request):
    """
    a function based view to show index page
    """
    return render(request,"index.html")
'''

class IndexView(TemplateView):
    """
    a class based view to show index page
    """
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Amin"
        context["posts"] = Post.objects.all()
        return context
    
''' FBV for redirect
from django.shortcuts import redirect
def RedirectToDjango(request):
    return redirect("https://www.djangoproject.com/") 
'''


class RedirectToDjango(RedirectView):
    url = 'https://www.djangoproject.com/'

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args, **kwargs)


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 2
    ordering = "-id"
    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
        
    #     return posts

class PostDetailView(DetailView):
    model = Post

'''

class PostCreateView(FormView):
    template_name = 'contact.html'
    form_class = PostForm
    success_url = '/blog/post/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
'''

class PostCreateView(CreateView):
    model = Post
    fields = ['author','title','content','status','category','published_date']
    success_url = "/blog/post/"