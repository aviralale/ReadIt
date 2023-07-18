from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from accounts.urls import *
from django.core.files.storage import default_storage
from django.urls import reverse
# Create your views here.


User = get_user_model()

@login_required
def account(request, username):
    user = get_object_or_404(User, username=username)
    
    try:
        user_profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=user)

    if request.method == 'POST':
        data = request.POST
        user_profile.facebook_username = data.get('facebook_username')
        user_profile.instagram_username = data.get('instagram_username')
        user_profile.linkedin_username = data.get('linkedin_username')
        user_profile.github_username = data.get('github_username')
        user_profile.youtube_username = data.get('youtube_username')
        user_profile.save()

        user.first_name = data.get('edit_profile_firstName')
        user.last_name = data.get('edit_profile_lastName')
        user.username = data.get('edit_profile_username')
        user.email = data.get('edit_profile_email')
        user.user_bio = data.get('edit_profile_user_bio')
        user.phone_number = data.get('edit_profile_phone')

        profile_picture = request.FILES.get('edit_profile_profile_pic')
        if profile_picture:
            # Delete existing profile picture if any
            if user.profile_picture:
                default_storage.delete(user.profile_picture.path)

            # Save the new profile picture
            user.profile_picture = profile_picture

        user.save()
        user_profile.save()

        return redirect(reverse('accounts:account', kwargs={'username': user.username}))

    context = {
        'profile_user': user,
        'current_user': request.user,
        'user_profile': user_profile
    }
    return render(request, 'account/account.html', context)