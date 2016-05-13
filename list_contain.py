def list_contains(value, c_list):
    for index, item in enumerate(c_list):
        if type(item) == type(c_list[index]):
            if item == c_list[index]:
                return True
    return False
