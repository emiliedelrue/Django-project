from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostForm
from .models import Comment


# Create your views here.


def post_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(BlogPost, pk=id )
    return render(request, 'post_detail.html', {'post': post})

def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = BlogPostForm()
    return render(request, 'create_post.html', {'form': form})


def edit_post(request, id):
    post = get_object_or_404(BlogPost, pk=id)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', id=post.id)
    else:
        form = BlogPostForm(instance=post)
    
    return render(request, 'edit_post.html', {'form': form, 'post': post})  # Ajoutez 'post': post ici


def add_comment(request, id):
    post = get_object_or_404(BlogPost, pk=id)
    if request.method == 'POST':
        author = request.POST.get('author')
        text = request.POST.get('text')
        Comment.objects.create(post=post, author=author, text=text)
        return redirect('post_detail', id=post.id)
    return render(request, 'add_comment.html', {'post': post})


def edit_comment(request, id, comment_id):
    post = get_object_or_404(BlogPost, pk=id)
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        comment.author = request.POST.get('author')
        comment.text = request.POST.get('text')
        comment.save()
        return redirect('post_detail', id=post.id)
    return render(request, 'edit_comment.html', {'comment': comment, 'post': post})


def delete_post(request, id):
    post = get_object_or_404(BlogPost, pk=id)
    post.delete()
    return redirect('post_list')


def delete_comment(request, id, comment_id):
    post = get_object_or_404(BlogPost, pk=id)
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('post_detail', id=post.id)