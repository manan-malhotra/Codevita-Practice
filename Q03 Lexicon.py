t = int(input())
while t != 0:
    p = input()
    s = input()
    op = ""
    for i in p:
        if i in s:
            op += i
    print(op)
    t -= 1
