from django.shortcuts import render, redirect
from .models import BlogPost, Author,CommentPost
from .forms import AddBlogPostForm, AddCommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
 

# Create your views here.


@login_required
def home_page(request):
    posts=BlogPost.objects.all()
    context={
        'posts':posts
    }
    # return render(request, "main/index.html", context) 
    response = render(request, "main/index.html", context)
    response.set_cookie('first_cookie', 'yoop my first http cookie')
    return response

 

def contact_page(request):
    return render(request, "main/contact.html")


def about_page(request):
    return render(request, "main/about.html")


def blog_detail_page(request, post_id):
    if not request.user.is_authenticated:
        return redirect('user-login')
    else:
        blog_post=BlogPost.objects.get(id=post_id)
        cookie=request.COOKIES.get('first_cookie')
    form=AddCommentForm()
    context={
        "post":blog_post,
        'comment_form':form,
        'first_cookie' :cookie
    }
    if request.method=="POST":
        form_data=AddCommentForm(request.POST)
        if form_data.is_valid():
            save_data=form_data.save(commit=False)
            save_data.post = blog_post
            save_data.save()
            messages.success(request, "comment added")
            return redirect ('blog-post.html', post_id=blog_post.id)
        

    return render(request, "main/post.html", context)



def post_page(request):
    return render(request, "main/post.html")




def author_profile_page(request, author_id):
  

    profile_page=Author.objects.get(id=author_id)
    context={

        "author":profile_page
    }
    return render(request, "main/profile.html", context)



def register_new_author(request):
    if request.method== 'POST':
        names=request.POST.get('names')
        email=request.POST.get("email")
        author = Author(names=names, email=email)
        author.save
        print(names)
        print(email)
    return render(request, 'main/new_author.html')


def addblogpost(request, author_id):
    form=AddBlogPostForm()
    author=Author.objects.get(id=author_id)
    context={
        "empty_form":form
    }
    if request.method == "POST":
        form_data=AddBlogPostForm(request.POST, request.FILES)
        if form_data.is_valid():
            title=form_data.cleaned_data.get('title')
            description=form_data.cleaned_data.get('description')
            content=form_data.cleaned_data.get('content')
            post_banner=form_data.cleaned_data.get('post_banner')
            owner= Author.objects.get(id=author_id)
            BlogPost.objects.create(title=title, description=description, content=content, owner=author, post_banner=post_banner)
            messages.success(request, "new post added successfully")
            return redirect("home-page")
    return render(request, "main/addpost.html", context) 




def addcomment(request, CommentPost):
    form=AddCommentForm()
    # author=Author.objects.get(id=author_id)
    comment=CommentPost.objects.get(id=CommentPost)
    context={
        "empty_form":form
    }
    if request.method == "POST":
        form_data=AddCommenntForm(request.POST, request.FILES)
        if form_data.is_valid():
            title=form_data.cleaned_data.get('title')
            description=form_data.cleaned_data.get('description')
            content=form_data.cleaned_data.get('content')
            post_banner=form_data.cleaned_data.get('post_banner')
            owner= CommentPost.objects.get(id=CommentPost)
            CommentPost.objects.create(title=title, description=description, content=content, owner=CommentPost, post_banner=post_banner)
            messages.success(request, "new comment added successfully")
            return redirect("about")
    return render(request, "main/about.html", context) 































# def addcommentpost(request):
#     post=post.objects.get()
#     comment= post.comment.all()
#     if request.method =='POST':
#         form =comment(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post=post
#             comment.auhtor=request.user
#             comment.save()
#             # messages.success(request, "new comment added successfully")
#             return redirect(request, 'main/post.html' )
        
#         else:
#             form = AddCommentForm()
#             return render(request, 'main/addpost.html', {'post':post, 'comments': comment, 'form':form,})
                           