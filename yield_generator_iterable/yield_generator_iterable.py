# When you create a list, you can read its items one by one, and it's called iteration

mylist = [1,2,3]
for i in mylist:
    print(i)

print("==================")
for j in mylist:
    print(j)


# Generators are iterators, but you can only iterate over them once
# they do not store all the values in memory, they generate the value on the fly:
mygenerator = (x**2 for x in range(3))
for i in mygenerator:
    print(i)

print("---------------")
print("generator can not be use for more than one time")
for j in mygenerator:
    print(j)


# yield is a keyword that used like return, except the function will return a generator
def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i * i

g = createGenerator()