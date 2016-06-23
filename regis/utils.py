from .models import UserProfile

def user_details(strategy, details, response, user=None, *args, **kwargs):
	if user:
		if kwargs['is_new']:
			attrs={'user':user}
			data={
			'first_name':details['first_name'],
			'last_name':details['last_name']
			}

			attrs=dict(attrs.items()+data.items())

			UserProfile.objects.create(**attrs)
