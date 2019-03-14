def test():
    a = 1
    b = 2
    huh = locals()
    c = 3
    print(huh)
    huh['d'] = 4
    print(d)