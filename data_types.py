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

my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9 , 10}

# print("difference: " + my_set.difference(your_set))
# print("discard: " + my_set.discard(4))
# print("difference_update: " + my_set.difference_update(your_set) ) #removes the different elements
# print("intersection: " + my_set.intersection(your_set))
# print("intersection 2: "+ my_set & your_set)
# print("isdisjoint: " + my_set.intersection(your_set)) # do sets have something in common
# print("issubset: " + my_set.issubset(your_set))
# print("issuperset: " + my_set.issuperset(your_set))
# print("union: " + my_set.union(your_set))
# print("union2: " + my_set | your_set)



#tuple - immutable lists
tuple1 = (1,2,3,4,6,0,7)
tuple2 = tuple(list1)

print("tuples")
print(tuple1)
print(tuple2)

new_list = [1,2,3,4,5,6,7,8,9,10]

def sum_list(any_list):
    counter = 0
    for item in any_list:
        counter = counter + item
    return counter

sum = sum_list(new_list)
print(sum)