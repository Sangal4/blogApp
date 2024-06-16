from django.urls import path
from . import views
from .views import home_view,post_detail,post_create,postUpdateView,postDeleteView, UserPostListView
urlpatterns = [
    path("",home_view.as_view(),name="home"),
    path("post/<int:pk>/",post_detail.as_view(),name="detailpost"),
    path("post/create",post_create.as_view(),name="createPost"),
    path("post/<int:pk>/update/",postUpdateView.as_view(),name="post-update"),
    path("post/<int:pk>/delete/",postDeleteView.as_view(),name="post-delete"),
    path("user/<str:username>/",UserPostListView.as_view(),name="user-posts"),
    path("about/",views.about,name="about"),
]
