from django import forms
from .models import KikoModel


# creating a form
class KikoForm(forms.ModelForm):

	# create meta class
	class Meta:
		# specify model to be used
		model = KikoModel

		# specify fields to be used
		fields = [
			"title",
			"description",
		]
