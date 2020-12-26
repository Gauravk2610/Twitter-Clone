from django.urls import path
from .views import ProfileListView, follow_unfollow_profile, ProfileDetailView, profile_save

app_name = 'profiles'

urlpatterns = [
    path('', ProfileListView.as_view(), name='profile-list-view'),
    path('siwtch_follow/', follow_unfollow_profile, name='follow-unfollow-profile'),
    path('<pk>/', ProfileDetailView.as_view(), name='profile-detail-view'),
    path('profile_save', profile_save, name="profile-save"),
]
