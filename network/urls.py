
from django.urls import path

from . import views

urlpatterns = [
    path("all-post", views.index, name="index"),
    path("", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('create-post', views.create_post, name='create_post'),
    path("like_post", views.like_post, name="like_post"),
    path("edit_post", views.edit_post, name="edit_post"),
    path("profile/<str:username>", views.profile, name="profile"),
    path("following", views.following, name="following"),
    path("toggle_follow", views.toggle_follow, name="toggle_follow")
]
