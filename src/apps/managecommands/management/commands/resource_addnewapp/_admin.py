from ._commons import validate_yes_no, MODELNAME_template

def create_admin(model_name):
	MODELNAME_template('admin', model_name)
	return

def request(model_name):
	while True:
		admin_required = input('Does this model require an admin.py [y/n] ')
		answer = validate_yes_no(admin_required)
		if answer:
			create_admin(model_name)
			return
		elif answer is None:
			pass
		elif not answer:
			return
