n = int(input())
time = int(input())
steps = []
winner_list = [0]*n
for _ in range(n):
    steps_list = list(map(int, input().split()))
    steps.append(steps_list)

sum_list = [0]*n
for s in range(2, time+1, 2):
    for r in range(n):
        sum_list[r] += (steps[r][s-2]+steps[r][s-1]*steps[r][time])
    maximum = max(sum_list)
    if(sum_list.count(maximum) > 1):
        for x in range(n):
            if (sum_list[x] == maximum):
                winner_list[x] += 1
    else:
        idx = sum_list.index(maximum)
        winner_list[idx] += 1
winner = max(winner_list)
print(winner_list.index(winner)+1)
