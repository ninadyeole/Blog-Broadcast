from django.shortcuts import render, HttpResponse, redirect
import os
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

#importing Models
from home.models import Contact, userInfo
from blog.models import Blog, blogComment

# Create your views here.
def HomeView(request) :
    allBlogs = Blog.objects.order_by('-views')[0:2]
    context = {'allBlogs': allBlogs}
    return render(request, 'home/home.html', context)


def ContactView(request) :
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<2 or len(email)<4 or len(phone)<10 or len(content)<4:
            messages.error(request, 'Please fill the form correctly')
        else: 
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, 'We have recieved your Message')

    return render(request, 'home/contact.html')

def search(request):
    query = request.GET['query']
    if len(query) > 80:
        allBlogs = Blog.objects.none()
    else:
        allBlogsTitle = Blog.objects.filter(title__icontains=query)
        allBlogsContent = Blog.objects.filter(content__icontains=query)
        allBlogs = allBlogsTitle.union(allBlogsContent)
    params = {'allBlogs': allBlogs, 'query': query}
    return render(request, 'home/search.html', params)

def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        #Check for error inputs
        if len(username)>15:
            messages.error(request, "Username has to be less than 15 characters")
            return redirect('/')
        if not username.isalnum(): 
            messages.error(request, "Username should contain only Letters and Numbers")
            return redirect('/')
        if pass1 != pass2 :
            messages.error(request, "Your passwords did not match")
            return redirect('/')

        #Create User
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your account has been created successfully")
        return redirect('/')

    else:
        return HttpResponse('Error 404 - Not Found')

def handleLogin(request):
    if request.method == 'POST':
        #Get Parameters
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        user = authenticate(username=loginusername, password=loginpass)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged in.")

        else:
            messages.error(request, "Your credentials were invalid. Please try again.")

        return redirect('/')

    else:
        return HttpResponse('Error 404 - Not Found')

def handleLogout(request):
        logout(request)
        messages.success(request, "Successfully Logged out.")
        return redirect('/')

def profileView(request):
    user = request.user
    allBlogs = Blog.objects.filter(author=user)[0:2]
    comments = blogComment.objects.filter(user=user)[0:2]

    if userInfo.objects.filter(user=user).count() > 0:
        userinfo = userInfo.objects.get(user=user)
        context = {'user': user, 'userinfo': userinfo, 'allBlogs': allBlogs, 'comments': comments}
    else:
        context = {'user': user, 'allBlogs': allBlogs, 'comments': comments}
    return render(request, 'home/profile.html', context)


def editProfileView(request):
    userinfo = userInfo.objects.get(user=request.user)
    print(userinfo)
    context = {'user': request.user, 'userinfo': userinfo}
    return render(request, 'home/editprofile.html', context)

def updateProfile(request):
    user = request.user
    fname = request.POST.get("f_name")
    lname = request.POST.get("l_name")
    email = request.POST.get("email")
    username = request.POST.get("username")
    bloglink = request.POST.get("bloglink")
    location = request.POST.get("location")
    about = request.POST.get("about")    
    user1 = User.objects.get(username=user.username)
    user1.first_name = fname
    user1.last_name = lname
    user1.email = email
    user1.username = username
    user1.save()
    if userInfo.objects.filter(user=user).count() == 0:
        userinfo1 = userInfo(user=user, bloglink=bloglink, about=about, location=location, pfp=request.FILES['photo'])
        userinfo1.save()
    else:
        userinfo1 = userInfo.objects.get(user=user)
        if len(request.FILES) != 0:
            if len(userinfo1.pfp) > 0:
                os.remove(userinfo1.pfp.path)
            userinfo1.pfp = request.FILES['photo']
        userinfo1.bloglink = bloglink
        userinfo1.about = about
        userinfo1.location = location
        userinfo1.save()
        
    return redirect('/profile')

def addBlog(request):
    context = {'user': request.user}
    return render(request, 'home/addBlog.html', context)

def saveBlog(request):
    if request.method=='POST':
        title = request.POST.get("title")
        slug = request.POST.get("slug")
        content = request.POST.get("content")
        newblog = Blog(author=request.user, title=title, slug=slug, content=content)
        newblog.save()

        return redirect('/profile')

def blogTutorial(request):
    return render(request, 'home/blogTutorial.html')