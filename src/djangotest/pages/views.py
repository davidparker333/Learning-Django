from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request, *args, **kwargs):
    # return HttpResponse("Hello world!")
    context = {}
    context["user"] = request.user
    return render(request, "home.html", context)

def add_post_view(request, *args, **kwargs):
    context = {}
    return render(request, 'addPost.html', context)