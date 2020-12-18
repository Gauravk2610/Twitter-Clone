from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user_name = models.TextField(User)
    profile_image = models.ImageField(upload_to="profile/images", blank=True)
    following = models.ManyToManyField(User, related_name='following', blank=True)
    bio = models.TextField(default="No Bio...")
    notification = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now=True)

    def profile_posts(self):
        return self.post_set.all()

    def __str__(self):
        return str(self.user.username)

    class Meta:
        ordering = ('-created',)