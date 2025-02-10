from django.shortcuts import render, redirect
from .forms import PostForm

# Create your views here.
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()


    return render(request, 'post_create.html', {'form': form})
