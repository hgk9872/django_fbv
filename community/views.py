from django.http import HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm, CommentForm


def index(request):
    post_list = Post.objects.order_by('-create_date')
    context = {'post_list': post_list}
    return render(request, 'community/post_list.html', context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'community/detail.html', context)


def comment_create(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) # 임시저장
            comment.post = post
            comment.save()
            return redirect('community:detail', post_id=post.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible')
    context = {'post': post, 'form': form}
    return render(request, 'community/detail.html', context)


def post_create(request):
    # 글 작성을 위해 POST 요청
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('community:index')
    else: # GET 요청
        form = PostForm() # empty form
    context = {'form': form}
    return render(request, 'community/post_form.html', context)
