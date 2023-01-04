n = int(input("Please enter the range of prime number you want"))
for x in (range(2, n)):
    if all(x % i != 0 for i in (range(2, x))):
        print(x)
