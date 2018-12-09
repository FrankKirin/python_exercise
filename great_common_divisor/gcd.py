def gcd(a, b):
    while b != 0:
       a, b = b, a%b
    return a


if __name__ == "__main__":
    res = gcd(16, 5)
    print(res)
