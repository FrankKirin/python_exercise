value1 = "cat"
value2 = "dog"

g = dict(globals())
for item in g.items():
    print(item[0], "=", item[1])
