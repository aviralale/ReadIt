from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact
from blog.models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout, authenticate
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your views here.


User = get_user_model()


# HTML TEMPS
def home(request):
    return render(request,'home/home.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        if len(name)<2 or len(email)<4 or len(phone)<10 or len(message)< 4:
            messages.error(request,'Your form has not been submitted. Please enter the right credentials and try again.')
        else:
            messages.success(request,'Your form has been submitted. We will reach to you soon.')

    
        contact = (Contact(
            name = name,
            email = email,
            phone = phone,
            message = message
        ))
        contact.save()
    return render(request,'home/contact.html')

def about(request):
    return render(request,'home/about.html')

def blogSearch(request):
    query = request.GET.get('query')
    if len(query)>69:
        allPosts= Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPostsAuthor = Post.objects.filter(author__icontains=query)
        allPostsCategory = Post.objects.filter(category__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent,allPostsAuthor,allPostsCategory)
    params = {'allPosts':allPosts,'query': query}
    return render(request,'blog/blogsearch.html',params)

# AUTH APIS
def handleSignup(request):
    if request.method == "POST":
        # GET POST PARAMETERS
        data = request.POST
        firstName = data.get('firstName')
        lastName = data.get('lastName')
        username = data.get('username')
        email = data.get('email')
        phone = data.get('phone')
        password1 = data.get('password1')
        password2 = data.get('password2')
        profile_pic = request.FILES.get('profile_pic')
        user = User.objects.filter(username = username)

        # CHECK FOR ERRORNEOUS I/P
        #usernname inder 20 characters and over 3
        if len(username) > 20 and len(username) < 3 :
            messages.error(request, "Your username should consist characters less than 20.")
            return redirect('home')
        #usernname should only consist of numbers and characters
        if not username.isalnum():
            messages.error(request, "Your username should only contain letters and numbers.")
            return redirect('home')
        # passwords should match
        if password1 != password2:
            messages.error(request, "Your passwords don't match.")
            return redirect('home')


        #Create user
        user = User.objects.create(username = username,
                                   first_name = firstName,
                                   last_name = lastName,
                                        email = email,
                                         profile_picture = profile_pic,
                                         phone_number = phone,
                                        password = password1,
                                        )
        user.set_password(password1)

        user.save()
        messages.success(request, "Your ReadIt account has been successfully created.")
        return redirect('home')
    else:
        return HttpResponse('404- Not Found')
    
def handleLogin(request):
    if request.method == "POST":
        loginUsername = request.POST.get('loginUsername')
        loginPassword = request.POST.get('loginPassword')
        user = authenticate(
            username=loginUsername,
            password=loginPassword
            )
        if user is not None:
            login(request, user)
            messages.success(request,'successfully logged in')
            return redirect('home')
        else:
            messages.error(request,"Invalid credentials. Please try again")
        return redirect('home')
    return HttpResponse("404 Not Found")

def handleLogout(request):
        logout(request)
        messages.success(request,'successfully logged out')
        return redirect('home')



