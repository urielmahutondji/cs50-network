from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import json
from .models import User, Posts, Follow

@login_required
def index(request):
    posts = Posts.objects.all().order_by('-timestamp')
    paginator = Paginator(posts, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, "network/index.html", {"page_obj": page_obj})

@login_required
def toggle_follow(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")

        try:
            target_user = User.objects.get(username=username)
        except User.DoesNotExist:
            return JsonResponse({"success": False, "error": "User not found"}, status=404)

        # Vérifie si déjà en follow
        follow = Follow.objects.filter(follower=request.user, following=target_user).first()
        if follow:
            follow.delete()
            is_following = False
        else:
            Follow.objects.create(follower=request.user, following=target_user)
            is_following = True

        return JsonResponse({
            "success": True,
            "is_following": is_following,
            "followers_count": target_user.followers.count()
        })

    return JsonResponse({"success": False}, status=400)

@login_required
def following(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    following_users = [follow.following for follow in request.user.following.all()]
    posts = Posts.objects.filter(user__in=following_users).order_by('-timestamp')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "network/following.html", {"page_obj": page_obj})

@login_required
def profile(request, username):
    try:
        profile_user = User.objects.get(username=username)
    except User.DoesNotExist:
        return HttpResponse("User not found", status=404)

    posts = Posts.objects.filter(user=profile_user).order_by('-timestamp')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    is_following = request.user.following.filter(following=profile_user).exists()
    followers_count = profile_user.followers.count()
    following_count = profile_user.following.count()

    return render(request, "network/profile.html", {
        "profile_user": profile_user,
        "page_obj": page_obj,
        "is_following": is_following,
        "followers_count": followers_count,
        "following_count": following_count
    })

@login_required
def edit_post(request):
    if request.method == "POST":
        data = json.loads(request.body)
        post_id = data.get("post_id")
        new_content = data.get("content")

        try:
            post = Posts.objects.get(id=post_id)
        except Posts.DoesNotExist:
            return JsonResponse({"success": False, "error": "Post not found"}, status=404)

        if request.user == post.user:
            post.content = new_content
            post.save()
            return JsonResponse({"success": True, "content": post.content})
        else:
            return JsonResponse({"success": False, "error": "Unauthorized"}, status=403)

    return JsonResponse({"success": False}, status=400)

@login_required
def like_post(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    data = json.loads(request.body)
    post_id = data.get("post_id")
    try:
        post = Posts.objects.get(id=post_id)
    except Posts.DoesNotExist:
        return JsonResponse({"error": "Post not found."}, status=404)
    user = request.user
    if user in post.likes.all():

        post.likes.remove(user)
        liked = False
    else:

        post.likes.add(user)
        liked = True
    return JsonResponse({
        "success": True,
        "liked": liked,
        "likes": post.likes.count()
    })

@login_required
def create_post(request):
    if request.method == "POST":
        content = request.POST.get("content", "")
        if content:
            post = Posts(user=request.user, content=content)
            post.save()
    return HttpResponseRedirect(reverse("index"))

def login_view(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))

    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
