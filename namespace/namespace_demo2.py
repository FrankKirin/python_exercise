def outer_func():
    c_num = 12
    def inner_func():
        d_num = 13
        print(dir(), ' - names in inner_func')
    e_num = 14
    inner_func()
    print(dir(), ' - names in inner_func')


if __name__ == '__main__':
    outer_func()

# result:
# d_num
# c_num, e_num, inner_func