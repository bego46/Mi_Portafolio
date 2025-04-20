from django.shortcuts import render, get_object_or_404, redirect
from .models import Proyecto, BlogPost
# from .forms import BlogPostForm, CommentForm

# Páginas básicas
def index(request):
    return render(request, 'web/index.html')
def about(request):
    return render(request, 'web/about.html')

def projects(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'web/projects/list.html', {'proyectos': proyectos})

# Blog
def blog(request):
    posts = BlogPost.objects.all().order_by('-fecha_publicacion')
    return render(request, 'web/blog/list.html', {'posts': posts})

def blog_post(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    # comments = Comment.objects.filter(post=post, aprobado=True)
    return render(request, 'web/blog/detail.html', {'post': post})

    """ if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog_post', post_id=post.id)
    else:
        form = CommentForm()
    
    return render(request, 'web/blog/detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
    }) """