
import requests

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.models import SocialToken

from testcambas.settings import FACEBOOK_API_URL


"""
List of pages with access
"""
def pages(fb_uid, token):
	returned_json = requests.get(FACEBOOK_API_URL + fb_uid + "/accounts?access_token=" + str(token))
	targets = returned_json.json()['data']
	id_list = [target['id'] for target in targets]
	return id_list

"""
Fan count, name, description from a page
"""
def general_info_page(id_page, token):
	returned_json = requests.get(FACEBOOK_API_URL + id_page + "/?fields=name,description,fan_count,picture&access_token=" + str(token))
	data = returned_json.json()
	return data

def photos_page(id_page, token):
	returned_json = requests.get(FACEBOOK_API_URL + id_page + "/fields?photos\{images\}&access_token=" + str(token))
	data = returned_json.json()['photos']
	photos_ = [photo['images'][0] for photo in data]
	return photos_

@login_required(login_url='/accounts/login/')
def page_info(request):
	args = {}
	fb_uid = SocialAccount.objects.filter(user_id=request.user.id, provider='facebook')
	if fb_uid.exists():
		fb_uid = fb_uid[0].uid
		token = SocialToken.objects.filter(account__user=request.user, account__provider='facebook').first()
		ids = pages(fb_uid, token)
		print (ids)
		if ids:
			id_page = ids[0]
			info = general_info_page(id_page, token)
			args['name'] = info['name']
			args['fan_count'] = info['fan_count']
			args['description'] = info['description']
			args['picture'] = info['picture']['data']['url']
			#args['photos'] = photos_page(id_page, token) # permissions issues
	return render(request, 'facebook/page_info.html', args)
