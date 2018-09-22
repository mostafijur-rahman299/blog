from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import (TemplateView,
                                  ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from apps.models import Post,Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from apps.forms import PostForm,CommentForm
from django.utils import timezone
# Create your views here.

class AboutPage(TemplateView):
    template_name='apps/about.html'

class PostList(ListView):
    model=Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetail(DetailView):
    model=Post

class PostCreate(LoginRequiredMixin,CreateView):
    form_class=PostForm
    login_url='/login/'
    model=Post
    redirect_field_name='apps/post_detail.html'

class PostUpdate(LoginRequiredMixin,UpdateView):
    form_class=PostForm
    login_url='/login/'
    model=Post
    redirect_field_name='apps/post_detail.html'

class PostDelete(LoginRequiredMixin,DeleteView):
    model=Post

    def get_success_url(self):
        return reverse('post_list')

class PostDraftList(LoginRequiredMixin,ListView):
    login_url='/login/'
    model=Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('create_date')


################################
##comment view system is here##
###############################

@login_required
def post_publish(request, pk):
    post=get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail',pk=post.pk)

@login_required
def add_comment_to_post(request, pk):
    post=get_object_or_404(Post, pk=pk)
    if request.method=='POST':
        form=CommentForm(data=request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form=CommentForm()
    return render(request,'apps/comment_form.html',{'form':form})


@login_required
def comment_approve(request, pk):
    comment=get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment=get_object_or_404(Comment,pk=pk)
    comment.delete()
    return redirect('post_detail',pk=comment.post.pk)
