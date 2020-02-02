some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

def find_duplicates(any_list):
    duplicates = []
    for val in any_list:
        if any_list.count(val) > 1:
            duplicates.append(val)
    if len(duplicates) > 0:       
        return duplicates
    else:
        return 'no duplicates'

duplicates = find_duplicates(some_list)