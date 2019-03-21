# The dir() function only outputs the list of names inside the current scope.

a_num = 10
print(dir())

def some_func():
    b_num = 11
    print(dir())

some_func()

print(dir())