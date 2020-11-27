from django.urls import path
from .views import posts_following_users, post_save, like_posts, tweet_detail, comment_save

app_name = 'posts'

urlpatterns = [
    path('', posts_following_users, name='posts-following-users'),
    path('post_save', post_save, name='post-save'),
    path('like/<pk>', like_posts, name='like-post'),
    path('comment', comment_save, name='comment-save'),
    path('<pk>', tweet_detail.as_view(), name='tweet-detail'),
]