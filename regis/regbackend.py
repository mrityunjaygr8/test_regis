from registration.backends.default.views import RegistrationView
from forms import UserProfileRegistrationForm
from models import UserProfile

class MyRegistrationView(RegistrationView):
	form_class = UserProfileRegistrationForm
	def register(self, form_class):
		new_user = super(MyRegistrationView,self).register(form_class)
		user_profile = UserProfile()
		user_profile.user = new_user
		user_profile.phone = form_class.cleaned_data['phone']
		user_profile.first_name = form_class.cleaned_data['first_name']
		user_profile.last_name = form_class.cleaned_data['last_name']
		user_profile.save()
		return user_profile
