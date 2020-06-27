t = int(input())
while t != 0:
    n = int(input())
    count = total = 0
    for i in range(n):
        if total < i:
            count += 1
            total += i
            i = total
    print(count)
    t -= 1
