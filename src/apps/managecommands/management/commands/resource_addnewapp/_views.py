import string
from ._commons import validate_yes_no, return_template, is_class_based
from . import _urls, _templates


def create_view(views_name, views_type, template_name, model_name=False):

    with open('views.py', 'a+b') as view_file:

        # If a model was previously created, add it as an import line
        if model_name:
            view_file.write(bytes('from models import {} \n'.format(model_name), 'UTF-8'))

        # Change template used depending on class or function based view
        if is_class_based(views_type):
            temp_id = 'cbv_views'
        else:
            temp_id = 'views'

        template = string.Template(open(return_template(temp_id)).read())
        variables = {
            'VIEWNAME':views_name,
            'TEMPLATENAME':template_name,
        }
        result = template.substitute(variables)

        view_file.write(bytes(result, 'UTF-8'))

        view_file.close()

    return

def request(app_name, model_name = False):
    while True:
        views_required = validate_yes_no(input('Does your app require a views.py [y/n]: '))
        if views_required:

            # Request name of view
            views_name = input('Enter the name of your view: ')
            if not views_name:
                views_name = 'MyView'

            # Request whether view should be classed based or function
            views_type = input('Is your view a) class based or b) a function [a/b]: ')

            # Check if view requires a template
            template_name = _templates.request(views_name)

            create_view(views_name, views_type, template_name, model_name)

            _urls.request(views_type, views_name)

            if template_name:
                _templates.create_template(template_name)

            return

        elif views_required is None:
            pass
        elif not views_required:
            return
