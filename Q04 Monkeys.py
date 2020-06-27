import math
t = input()
while(t != 0):
    n = int(input())
    monkey = list(map(int, input().split()))
    steps = set()
    monkey.insert(0, 0)
    for i in range(1, n+1):
        if(monkey[i] == 0):
            continue
        count = 0
        current = i
        block = i
        while(True):
            current = monkey[current]
            monkey[block] = 0
            block = current
            count += 1
            if (current == 1):
                break
        steps.add(count)

    if(len(steps) == 1):
        for x in steps:
            print(x)
    else:
        lcm = steps[0]
        for i in range(1, len(steps)):
            lcm = lcm*steps[i]//math.gcd(lcm, steps[i])
        print(lcm)
        t -= 1
