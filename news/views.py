from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Author
from django.utils.timezone import localtime

def home_view(request):
    posts = Post.objects.order_by('-created_at')
    best_user = Post.objects.filter(author__rating__isnull=False).order_by('-author__rating').first()
    best_post = Post.objects.order_by('-rating').first()
    comments = best_post.comments.all() if best_post else []

    context = {
        'posts': posts,
        'best_user': best_user.author if best_user else None,
        'best_post': best_post,
        'comments': comments,
    }
    return render(request, 'home.html', context)

def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.rating += 1
    post.save()
    return redirect('home')

def dislike_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.rating -= 1
    post.save()
    return redirect('home')

def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.rating += 1
    comment.save()
    return redirect('home')

def dislike_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.rating -= 1
    comment.save()
    return redirect('home')

def news_list(request):
    posts = Post.objects.order_by('-created_at')
    context = {'posts': posts}
    return render(request, 'news_list.html', context)

def news_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {
        'post': post,
        'formatted_date': localtime(post.created_at).strftime('%d.%m.%Y')
    }
    return render(request, 'news_detail.html', context)