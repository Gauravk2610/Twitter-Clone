from django.shortcuts import render
from profiles.models import Profile
from .models import Notify

# Create your views here.
def notify_info(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    profile.notification = False
    profile.save()
    notification = profile.notify_set.all()
    print(notification)
    return render(request, 'notify.html', {'profile':profile, 'notification': notification})