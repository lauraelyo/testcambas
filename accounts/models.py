from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.db.models.signals import post_save
from django.dispatch import receiver

from allauth.account.signals import user_signed_up

 
# Create your models here.
 
class UserProfileManager(models.Manager):
	pass
 
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	description = models.CharField(max_length=100, default='')
	city = models.CharField(max_length=100, default='')
	website = models.URLField(default='')
	phoneNumber = models.IntegerField(default=0)
 
	def __str__(self):
		return self.user.username
 
@receiver(user_signed_up)
def create_user_profile(request, user, **kwargs):
    profile = UserProfile.objects.create(user=user)
    profile.save()  