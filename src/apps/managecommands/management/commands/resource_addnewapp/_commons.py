import os, string

def validate_yes_no(answer):
	VALIDATION_TABLE = {'y':True, 'n':False, 'yes':True, 'no':True, 'Y':True, 'N':False}
	try:
		return VALIDATION_TABLE[answer]
	except KeyError:
		return None

def return_template(component):
	cur_dir = os.path.dirname(os.path.realpath(__file__))
	return os.path.join(cur_dir, 'templates', '_%s.template' % component)

def MODELNAME_template(filename, model_name):
	template = string.Template(open(return_template(filename)).read())
	variables = {'MODELNAME':model_name}
	result = template.substitute(variables)
	with open('%s.py' % filename, 'a+b') as model_file:
		model_file.write(bytes(result, 'UTF-8'))
		model_file.close()
	return

def is_class_based(view_type):
	return True if view_type in ('a', 'A', 'class') else False
