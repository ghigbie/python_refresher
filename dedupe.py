some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
non_dupe = ['moo', 'meow', 'woof']

def find_duplicates(any_list):
    duplicates = []
    for val in any_list:     
        if any_list.count(val) > 1:
            if val not in duplicates:
                duplicates.append(val)
    if len(duplicates) > 0:       
        return duplicates
    else:
        return 'no duplicates'
        
print(find_duplicates(some_list))
print(find_duplicates(non_dupe))

