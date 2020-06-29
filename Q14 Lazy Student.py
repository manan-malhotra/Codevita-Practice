from math import factorial as f


def modInverse(a, m):
    a = a % m
    for x in range(1, m):
        if ((a * x) % m == 1):
            return x
    return 1


n = int(input())
t = int(input())
m = int(input())
u = n-m
den = f(n)*f(u-t)
num = den-(f(u)*f(n-t))
mod = 1000000007
ans = modInverse(den, mod)
print(num*ans)
print(num/den)
