import sys, os
from importlib import import_module
from ._commons import validate_yes_no, MODELNAME_template
from . import _admin

def create_model(model_name):
	MODELNAME_template('models', model_name)
	return

def request(app_name):
	while True:
		model_required = validate_yes_no(input('Does your app require a models.py [y/n]: '))
		if model_required:
			model_name = input('What is the name of your model? ')
			# Default model name if none supplied
			if not model_name:
				model_name = "MyModel"

			# Check if abstract base fields and include them as inherited model if they exist
			# try:
			# 	from libs.utils.abstract_models import BaseFields
			# except ImportError:
			# 	pass

			create_model(model_name)

			# Ask if an admin for this model should be created
			_admin.request(model_name)

			return model_name

			# Check if additional models should be appended to models.py
			# additional_model = validate_yes_no(raw_input('Is an additional model needed [y/n] '))
			# if additional_model:
			# 	pass
			# elif additional_model is None:
			# 	sys.stdout.write('Response not recognised. No additional models have been created')
			# 	break
			# elif not model_required:
			# 	break

		elif model_required is None:
			# If non-sensical response given to model_required, pass and repeat while loop
			pass
		elif not model_required:
			# If no model required, return from _models.request
			return False
