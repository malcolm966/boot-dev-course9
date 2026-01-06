def does_name_exist(first_names, last_names, full_name):
    for f in first_names:
        for l in last_names:
            if full_name == f + l:
                return True
    return False