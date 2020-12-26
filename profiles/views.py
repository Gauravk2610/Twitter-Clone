from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Profile
# Create your views here.

class ProfileListView(ListView):
    model = Profile
    template_name = "connect.html"
    context_object_name = 'profiles'

    def get_queryset(self):
        return Profile.objects.all().exclude(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        profile =  Profile.objects.get(user=user)
        context["prof_user"] = profile
        return context
    
def follow_unfollow_profile(request):
    if request.method == "POST":
        my_profile = Profile.objects.get(user=request.user)
        pk = request.POST.get("profile_pk")
        obj = Profile.objects.get(pk=pk)

        if obj.user in my_profile.following.all():
            my_profile.following.remove(obj.user)

        else:
            my_profile.following.add(obj.user)
        
        return redirect(request.META.get('HTTP_REFERER'))

    return redirect('profiles:profile-list-view')

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile.html'
    
    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        view_profile = Profile.objects.get(pk=pk)
        return view_profile
        # return super().get_object()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        profile =  Profile.objects.get(user=user)
        context["prof_user"] = profile
        return context

'''def index(request):
    prof_list = []
    profiles = Profile.objects.all().exclude(user=request.user)
    view_profile = request.user
    for profile in profiles:
        if view_profile in profiles.following.all():
            prof_list.append
'''