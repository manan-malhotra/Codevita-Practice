def isPrime(n):
    count = 0
    for i in range(2, int(n**0.5+1)):
        if n % i == 0:
            count += 1
            continue
    if count == 0:
        return True
    return False


a, b = map(int, input().split())
primeNo = []
for i in range(a, b+1):
    if (isPrime(i)):
        primeNo.append(i)
combo = set()
for i, e1 in enumerate(primeNo):
    for j, e2 in enumerate(primeNo):
        if i != j:
            el = int(str(e1)+str(e2))
            if isPrime(el):
                combo.add(el)
f1 = min(combo)
f2 = max(combo)
length = len(combo)
fib = [f1, f2]
while length-2 != 0:
    f3 = f1 + f2
    f1, f2 = f2, f3
    length -= 1
    fib.append(f3)
print(fib[-1])
