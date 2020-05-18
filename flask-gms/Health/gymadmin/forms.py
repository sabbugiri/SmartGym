from django import forms

from gyms.models import Gym,User


class GymForm(forms.Form):
	name = forms.CharField(max_length = 200)
	location = forms.CharField(max_length = 200)
	price = forms.IntegerField(label = "Average Cost")
	summary = forms.CharField(widget = forms.Textarea, required = False)
	featured_photo = forms.ImageField(required = False)
	user = forms.IntegerField(help_text = "Please enter a valid user Id. This will be chnaged in future.")


	def clean_price(self):
		price = self.cleaned_data['price']
		if price < 200:
			raise ValidationError("Price can't be less than {}.".format(price))
		return price
		

	def clean_user(self):
		gym = Gym.objects.create(
			name = self.cleaned_data["name"],
			location = self.cleaned_data["location"],
			price = self.cleaned_data["price"],
			summary = self.cleaned_data["summary"],
			featured_photo = self.cleaned_data["featured_photo"],
			user = self.cleaned_data["user"],


			)	

		return gym		




