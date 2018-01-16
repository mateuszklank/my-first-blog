from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .models import Post
from .models import Lekarz
from .models import Galeria
from .forms import PostForm
from .forms import LekarzForm

# Create your views here.

def lekarz_list(request):
    lekarze = Lekarz.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/lekarz_list.html', {'lekarze': lekarze})

def lekarz_detail(request, pk):
    lekarz = get_object_or_404(Lekarz, pk=pk)
    return render(request, 'blog/lekarz_detail.html', {'lekarz': lekarz})

def lekarz_new(request):
    if request.method == "POST":
        form = LekarzForm(request.POST)
        if form.is_valid():
            lekarz = form.save(commit=False)
            lekarz.author = request.user
            lekarz.published_date = timezone.now()
            lekarz.save()
            return redirect('lekarz_detail', pk=lekarz.pk)
    else:
        form = LekarzForm()
    return render(request, 'blog/lekarz_edit.html', {'form': form})

def lekarz_edit(request, pk):
    lekarz = get_object_or_404(Lekarz, pk=pk)
    if request.method == "POST":
        form = LekarzForm(request.POST, instance=lekarz)
        if form.is_valid():
            lekarz = form.save(commit=False)
            lekarz.author = request.user
            lekarz.published_date = timezone.now()
            lekarz.save()
            return redirect('lekarz_detail', pk=lekarz.pk)
    else:
        form = LekarzForm(instance=lekarz)
    return render(request, 'blog/lekarz_edit.html', {'form': form})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def galeria(request):
    #galeria = get_object_or_404(Galeria)
    return render(request, 'blog/galeria.html', {'galeria': galeria})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})