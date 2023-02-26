from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='posts_hhome'),
    path("greet/", views.greet, name="greet_name"),
    path("posts/",views.return_all_posts, name="all_posts"),
    path("posts/<int:post_id>/",views.return_one_post, name="get_one_posts")
]  
