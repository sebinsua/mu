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
    return all
