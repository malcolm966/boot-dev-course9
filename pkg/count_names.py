def count_names(list_of_lists, target_name):
    name_count = 0
    for list in list_of_lists:
        for name in list:
            if name == target_name:
                name_count += 1
    return name_count
