from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from blog.forms import NewPostForm
from blog.models import Post

def home_view(request, *args, **kwargs):
    # return HttpResponse("Hello world!")
    context = {}
    context["user"] = request.user
    return render(request, "home.html", context)

def add_post_view(request, *args, **kwargs):
    context = {}
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            # If I was using a regular form, not model form
            # title = form.cleaned_data['title']
            # body = form.cleaned_data['body']
            # p = Post(title=title, body=body)
            # p.save()
            form.save()
            return render(request, 'home.html', context)
    else:
        form = NewPostForm()
        context['form'] = form
    return render(request, 'addPost.html', context)