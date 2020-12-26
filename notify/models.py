from django.db import models
from posts.models import Post
from profiles.models import Profile
# Create your models here.
class Notify(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.post.author)
    

    class Meta:
        ordering = ('-created',)
