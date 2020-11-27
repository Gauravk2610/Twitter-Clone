from django.db import models
from profiles.models import Profile
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    body = models.TextField()
    hastag = models.TextField(blank=True)
    post_image = models.ImageField(default=False)
    link = models.URLField(blank=True, max_length = 200)
    liked = models.ManyToManyField(User, default=None, blank=True, related_name="liked")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.body)[:30]

    def comments(self):
        return self.comment_set.all()

    class Meta:
        ordering = ('-created',)
    
    @property
    def num_likes(self):
        return self.liked.all().count()

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike')
)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES ,default='Like', max_length=10)

    def __str__(self):
        return str(self.post)

class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)

    def __str__(self):
        return str(self.comment)[:30]    