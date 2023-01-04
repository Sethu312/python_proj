for x in range(2, 10):
    if all(x % i != 0 for i in range(2, x)):
        print(x)
