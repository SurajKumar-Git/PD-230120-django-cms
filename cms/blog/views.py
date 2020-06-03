from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from blog.forms import ContactUsForm
# Create your views here.

# def index(request):
#     return HttpResponse("Welcome to my blog!!!")

def index(request):
    posts = Post.objects.all()
    return render(request,"blog/stories.html",context = {"posts":posts})

# def index2(request):
#     return render(request,"temp.html")

def post_details(request,id):
    try:
        post = Post.objects.get(id = id)
        return render(request,"blog/blog-post.html",context = {"post":post})
    except:
        return HttpResponse("Welcome to my blog!!!")


def contact_us_form_view(request):
    # print(request.method)
    # print(request.GET)
    if request.method == "GET":
        form = ContactUsForm()
        return render(request,"blog/contact-us.html",context = {"form":form})
    else:

        form = ContactUsForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponse("Thank you for submitting the response")
        else:
            print(form.errors)
            return render(request,"blog/contact-us.html",context = {"form":form})
        




# blog 
#     \static
#         \blog 
#             images 
#                a.jpeg 

# 127.0.0.1:8000/static/a.jpeg 
