from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from home.models import userInfo
from blog.models import Blog, blogComment
from django.contrib import messages
from blog.templatetags import extras

# Create your views here.

def blogHomeView(request) :
    allBlogs = Blog.objects.order_by('-views')
    context = {'allBlogs': allBlogs}
    return render(request, 'blog/blogHome.html', context)

def blogView(request, slug):
    blog = Blog.objects.filter(slug=slug).first()
    blog.views = blog.views + 1
    blog.save() 

    comments = blogComment.objects.filter(blog=blog, parent=None)
    replies = blogComment.objects.filter(blog=blog).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    print(replyDict)
    context = {'blog': blog, 'comments': comments, 'user': request.user, 'replyDict': replyDict}
    return render(request, 'blog/blogpost.html', context)

def postComment(request):
    if request.method=="POST":
        comment = request.POST.get("comment")
        parentSno = request.POST.get("parentSno")
        user = request.user
        blogSno = request.POST.get("blogSno")
        blog = Blog.objects.get(sno=blogSno)
        if parentSno == "":    
            comment = blogComment(comment=comment, user=user, blog=blog)
            messages.success(request, "Your comment has been succesfully displayed")
        else:
            parent = blogComment.objects.get(sno=parentSno)
            comment = blogComment(comment=comment, user=user, blog=blog, parent=parent)
            messages.success(request, "Your reply has been succesfully displayed")
        
        comment.save()
        return redirect(f"/blog/{blog.slug}")
    return HttpResponse('Error 404')


def yourBlogs(request):
    user = request.user
    allBlogs = Blog.objects.filter(author=user)
    context = {'allBlogs': allBlogs}

    return render(request, 'blog/yourblogs.html', context)


def yourComments(request):
    user = request.user
    comments = blogComment.objects.filter(user=user)
    context = {'comments': comments}

    return render(request, 'blog/yourcomments.html', context)