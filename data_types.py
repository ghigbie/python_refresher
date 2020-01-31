#lists - a collection of elements
list1 = ['moo', 'woof', 'meow']
list2 = list('moo')

print("lists")
print(list1)
print(list2)

#set - a dedupped list that orderd
set1 = {1, 2, 3, 4, 5, 5, 5}
set2 = set(list1)
set3 = {4, 3, 1, 8, 0}

print("sets")
print(set1)
print(set2)
print(set3)

#tuple - immutable lists
tuple1 = (1,2,3,4,6,0,7)
tuple2 = tuple(list1)

print("tuples")
print(tuple1)
print(tuple2)