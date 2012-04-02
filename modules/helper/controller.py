controller_dict = {}

def generate_controller_list(file_name):
    from os import path, listdir

    module_directory = path.dirname(file_name)
    reject = ['tmp', 'swp', 'py', 'pyc', '__init__', '']

    temp_items = []
    for item_path in listdir(module_directory):
        item_path = item_path.rsplit('.')
        temp_items.extend(item_path)

    all_with_duplicates = filter(lambda item: item not in reject, temp_items)

    all = list(set(all_with_duplicates))

    build_controller_dict(module_directory, all)

    return all


def build_controller_dict(module_directory, controller_list):
    global controller_dict

    import os

    module_name = ''
    tail = module_directory
    head = ''
    while head != 'controller':
        path = os.path.split(tail)
        tail = path[0]
        head = path[1]
        if module_name == '':
            module_name = head
            continue
        if head != '':
            module_name = head + '.' + module_name

    controller_dict[module_name] = controller_list


def generate_blueprint_list(controller_dict):
    blueprints = []
    for module_key in controller_dict:
        for controller in controller_dict[module_key]:
            blueprint_var_name = 'bp'
            blueprint = module_key + '.' + controller + '.' + blueprint_var_name
            blueprints.append(blueprint)
    return blueprints


def register_controller_blueprints(app, controller):
    from flask import Blueprint

    global controller_dict
    blueprint_list = generate_blueprint_list(controller_dict)
    for blueprint_name in blueprint_list:
        try:
            # NOTE: We needed to pass in the controller module due to the access
            # by eval() below.
            blueprint = eval(blueprint_name)
            if isinstance(blueprint, Blueprint):
                app.register_blueprint(blueprint)
        except:
            continue
