list_a = [1, 2, 3, 4, 5]
list_b = ['a', 'b', 'c', 'd', 'e']

# python3, zip method return a zip object instead of a list
# this zip object is an iterator. Iterator are lazily evaluated
# len function can not use with iterator
# loop over the zip object to get the actual list
zipped_list = zip(list_a, list_b)

print(zipped_list)

# unzip a list of tuple
list_a, list_b = zip(*zipped_list)
print(list_a)
print(list_b)