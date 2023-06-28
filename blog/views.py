from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseBadRequest
from blog.models import Post,blogComment
from django.contrib import messages
from blog.templatetags import get_dict

# Create your views here.
def blogHome(request):
    # order_by('-timeStamp'), the minus sign (-) is used as a prefix to indicate descending order based on the timeStamp field.
    allPosts = Post.objects.order_by('-views')
    top_viewed_posts = Post.objects.order_by('-views')
    context ={
                'allPosts':allPosts,
              'top_viewed_posts': top_viewed_posts,
              }

    return render(request,'blog/blogHome.html',context)



def blogPost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    post.views = post.views + 1
    post.save()
    top_viewed_posts = Post.objects.order_by('-views')
    comments = blogComment.objects.filter(post=post,parent=None)
    replies = blogComment.objects.filter(post=post).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    # print(comments,replies)
    print(replyDict)
    context={'post':post,
             'comments': comments,
             'user': request.user,
             'replyDict':replyDict,
             'top_viewed_posts': top_viewed_posts,
             }
    return render(request,'blog/blogpost.html',context)

def display_post_with_highest_views(request):
    highest_views_post = Post.objects.order_by('-views').first()
    return render(request, 'blogHome.html', {'post': highest_views_post})


def postComment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        if not comment:
            messages.warning(request,"Comment cannot be empty.")
        user = request.user
        postSN = request.POST.get('postSN')
        post = Post.objects.get(sno=postSN)
        parentSN = request.POST.get("parentSN")
        if parentSN == "":
            comment = blogComment(
                            comment=comment,
                            user=user,
                            post=post,
                            )
            comment.save()
            messages.success(request,"Your comment has been posted successfully")                
        else:
            parent = blogComment.objects.get(sno=parentSN)
            comment = blogComment(
                            comment=comment,
                            user=user,
                            post=post,
                            parent=parent,
                            )
            comment.save()
            messages.success(request,"Your reply has been posted successfully")

    return redirect(f"/blog/{post.slug}")

def category_world(request):
    posts = Post.objects.filter(category='world')
    return render(request, 'blog/blogCategory.html', {'category': 'World', 'posts': posts})

def category_us(request):
    posts = Post.objects.filter(category='us')
    return render(request, 'blog/blogCategory.html', {'category': 'U.S.', 'posts': posts})

def category_technology(request):
    posts = Post.objects.filter(category='technology')
    return render(request, 'blog/blogCategory.html', {'category': 'Technology', 'posts': posts})

def category_design(request):
    posts = Post.objects.filter(category='design')
    return render(request, 'blog/blogCategory.html', {'category': 'Design', 'posts': posts})

def category_culture(request):
    posts = Post.objects.filter(category='culture')
    return render(request, 'blog/blogCategory.html', {'category': 'Culture', 'posts': posts})

def category_business(request):
    posts = Post.objects.filter(category='business')
    return render(request, 'blog/blogCategory.html', {'category': 'Business', 'posts': posts})

def category_politics(request):
    posts = Post.objects.filter(category='politics')
    return render(request, 'blog/blogCategory.html', {'category': 'Politics', 'posts': posts})

def category_opinion(request):
    posts = Post.objects.filter(category='opinion')
    return render(request, 'blog/blogCategory.html', {'category': 'Opinion', 'posts': posts})

def category_science(request):
    posts = Post.objects.filter(category='science')
    return render(request, 'blog/blogCategory.html', {'category': 'Science', 'posts': posts})

def category_health(request):
    posts = Post.objects.filter(category='health')
    return render(request, 'blog/blogCategory.html', {'category': 'Health', 'posts': posts})

def category_style(request):
    posts = Post.objects.filter(category='style')
    return render(request, 'blog/blogCategory.html', {'category': 'Style', 'posts': posts})

def category_travel(request):
    posts = Post.objects.filter(category='travel')
    return render(request, 'blog/blogCategory.html', {'category': 'Travel', 'posts': posts})

