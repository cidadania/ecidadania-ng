import os
from ._commons import validate_yes_no

def create_template(template_name):

	template_dir = os.path.join(os.getcwd(), 'templates')
	template_location = os.path.join(os.getcwd(), 'templates', '%s.html' % template_name)

	# Create template dir for this app, if it does not exist
	if not os.path.exists(template_dir):
		os.makedirs(template_dir)

	# Touch open the template
	open(template_location, 'a').close()

	return

def request(view_name):
	while True:
		templates_required = validate_yes_no(input('Does your view require a template [y/n]: '))
		if templates_required:

			# Request name of template
			template_name = input('Enter the name of your template: ')
			if not template_name:
				template_name = '%s.html' % view_name

			# create_template(views_name, views_type, model_name)

			return template_name

		elif templates_required is None:
			pass
		elif not templates_required:
			return False
