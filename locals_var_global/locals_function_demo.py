# locals() function returns a dictionary containing the variables defined in local namespace

from pprint import pprint

a = 10
b = 20

def foo():
    x = 30
    y = 40
    print("locals() = {}".format(locals()))

pprint(locals())

print("*" * 80)

print("locals() == globals()? ", locals()==globals())

print("*" * 80)

foo()