from datetime import datetime

from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from accounts.forms import (EditProfileForm, ProfileForm)

 
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid() and profile_form.is_valid():
            user_form = form.save()
            custom_form = profile_form.save(False)
            custom_form.user = user_form
            custom_form.save()
            messages.add_message(
			    request, messages.SUCCESS, 'Profile details updated.',
			    fail_silently=True,
			)

            return redirect('accounts:edit_profile')
    else:
        form = EditProfileForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.userprofile)
        args = {}
        args['form'] = form
        args['profile_form'] = profile_form
        return render(request, 'account/edit_profile.html', args)