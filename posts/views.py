from django.shortcuts import render, redirect, HttpResponse
from profiles.models import Profile
from django.views.generic import DetailView
from posts.models import Post, Comment
from itertools import chain

# Create your views here.

def posts_following_users(request):
    profile = Profile.objects.get(user=request.user)
    users = [user for user in profile.following.all()]
    posts = []
    qs = None

    for u in users:
        p = Profile.objects.get(user=u)
        p_posts = p.profile_posts()
        posts.append(p_posts)

    my_posts = profile.profile_posts()
    posts.append(my_posts)

    if len(posts) > 0:
        qs = sorted(chain(*posts), reverse=True, key=lambda obj:obj.created)
    return render(request, 'posts.html', {'profile':profile, 'posts':qs})

def post_save(request):
    if request.method == 'POST':
        pk = request.POST.get("profile_pk")
        body = request.POST.get('text1')
        img_file = request.FILES['imgInp']
        img = request.POST.get('imgInp') 
        profile = Profile.objects.get(user=request.user)
        post = Post(author=profile, body=body, post_image=img_file)
        post.save()
        print(pk, body, img)
    return redirect(request.META.get('HTTP_REFERER'))

def like_posts(request, pk):
    user = request.user
    post = Post.objects.get(pk=pk)

    if user in post.liked.all():
        post.liked.remove(user)
    else:
        post.liked.add(user)
    # return redirect('posts:post-like')
    return redirect(request.META.get('HTTP_REFERER'))

def comment_save(request):
    if request.method == "POST":
        profile = Profile.objects.get(user=request.user)
        pk = request.POST.get("post_pk")
        post = Post.objects.get(pk=pk)
        content = request.POST.get('content')
        if bool(content) != False: 
            comment = Comment(user=profile, post=post, comment=content)
            comment.save()
        print(post.body)
        print(pk, content)
        print(bool(content))
        return redirect(request.META.get('HTTP_REFERER'))
        
class tweet_detail(DetailView):
    model = Post
    template_name = 'tweet_detail.html'
    context_object_name = 'post'

    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        print(pk)
        post = Post.objects.get(pk=pk)
        return post