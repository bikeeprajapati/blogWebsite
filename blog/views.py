from django.shortcuts import render , redirect,get_object_or_404, redirect
from .models import PostModel
from .forms import PostModelForm , PostUpdateForm

# Create your views here.
def index(request):
    posts = PostModel.objects.all()
    form = PostModelForm() 
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
           instance = form.save(commit=False)
           instance.author = request.user
           instance.save()
           return redirect('blog-index')
        
    context ={
        'posts': posts,
        'form': form
    }
    return render(request, 'blog/index.html',context)

def post_detail(request,pk):
    post =PostModel.objects.get(id=pk)
    context={
        'post': post
        
        
    }
    return render(request, 'blog/post_detail.html',context)


def post_edit(request, pk):
    # Retrieve the post or return a 404 error if it doesn't exist
    post = get_object_or_404(PostModel, id=pk)

    if request.method == "POST":
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog-post-detail', pk=post.pk)  # Redirect to the detailed view of the post
    else:
        # Display the form with the post data pre-filled
        form = PostUpdateForm(instance=post)

    # Pass the form to the template
    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'blog/post_edit.html', context)

def post_delete(request, pk):
    post = get_object_or_404(PostModel, id=pk)
    if request.method == "POST":
        post.delete()
        return redirect('blog-index')  
    return render(request, 'blog/post_delete.html', {'post': post})
