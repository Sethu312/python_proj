def F(n):
    if n == 0: return 0
    if n == 1: return 1
    else: return F(n-1) + F(n-2)

for n in range(0,10):
    print(F(n))