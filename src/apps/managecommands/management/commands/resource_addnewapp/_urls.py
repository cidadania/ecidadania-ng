import string
from ._commons import validate_yes_no, return_template, is_class_based

def create_urls(views_type, view_name):

	with open('urls.py', 'a+b') as urls_file:

		if is_class_based(views_type):
			temp_id = 'cbv_urls'
		else:
			temp_id = 'urls'

		template = string.Template(open(return_template(temp_id)).read())
		variables = {'VIEWNAME':view_name}
		result = template.substitute(variables)

		urls_file.write(bytes(result, 'UTF-8'))
		urls_file.close()

	return

def request(views_type, view_name):
	while True:
		urls_required = validate_yes_no(input('Do your views require a urls.py [y/n]: '))
		if urls_required:
			create_urls(views_type, view_name)
			return

		elif urls_required is None:
			pass
		elif not urls_required:
			return
