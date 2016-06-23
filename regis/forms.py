from registration.forms import RegistrationFormUniqueEmail
from django import forms
class UserProfileRegistrationForm(RegistrationFormUniqueEmail):
	phone = forms.CharField()

	first_name = forms.CharField()
	last_name = forms.CharField()
	