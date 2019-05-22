from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
from django.forms import ModelForm
 
from accounts.models import UserProfile
 
class EditProfileForm(ModelForm):
    class Meta:
        model = User
        fields = (
         'email',
         'first_name',  
         'last_name'
        )

class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('city', 'description', 'phoneNumber', 'website')