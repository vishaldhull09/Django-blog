from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse , Http404
from .models import Post
from django.core.paginator import Paginator 
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# Create your views here.


def home( request ):
	context = {
	'posts':Post.objects.all()
	}
	return render( request,'vi.html',context)

class PostListView(ListView):
	model=Post
	template_name = 'vi.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 3

class PostDetailView(DetailView):
	model=Post
	template_name = 'post_detai.html'
	

class PostCreateView(LoginRequiredMixin,CreateView):
	model=Post
	fields = ['title','content']
	template_name = 'post_form.html'

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model=Post
	fields = ['title','content']
	template_name = 'post_form.html'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False
			
	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model=Post
	template_name = 'post_confirm_delete.html'

	success_url = '/home/'


	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False





def about( request ):
	return render( request,'about.html',{'title':'About'})	