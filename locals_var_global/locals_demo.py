def demo1():
    print("Here no local variable is present : ", locals())

def demo2():
    name = "Ankit"
    print("Here local variables are present : ", locals())


demo1()
demo2()


def demo3():
    print("Here no local variable is present : ", locals())

def demo4():
    name = "Ankit"
    print("Here local variables are present : ", locals())
    print("Before updating name is : ", name)

    locals()["name"] = "Sri Ram"

    print("After updating name is : ", name)

demo3()
demo4() 