
# ! Alternate Solution (Longer)
def To_find_Pime_Numbers(element):
    if(element == 1):
        return False
    elif(element == 2):
        return True
    elif(element != 2 and element % 2 == 0):  # bcoz a even number will not be the prime number
        return False
    else:
        count = 0
        for i in range(2, int(element**0.5+1)):
            if(element % i == 0):
                count += 1
        if(count == 0):
            return True
        # else:
        return False


a, b = input().split()
element1 = int(a)
element2 = int(b)
prime_nums = []
for i in range(element1, element2+1):
    primenumber = To_find_Pime_Numbers(i)
    if(primenumber == True):
        prime_nums.append(i)
combo_list = []
for i, v1 in enumerate(prime_nums):
    for j, v2 in enumerate(prime_nums):
        if(i != j):
            element = int(str(v1)+str(v2))
            req_ele = To_find_Pime_Numbers(element)
            if(req_ele == True):
                combo_list.append(element)
prime_nums.clear()
fib1 = min(combo_list)
fib2 = max(combo_list)
length = len(sorted(set(combo_list)))
combo_list.clear()
fib_series = [fib1, fib2]
while(length-2 != 0):
    fib3 = fib1+fib2
    fib1 = fib2
    fib2 = fib3
    length -= 1
    fib_series.append(fib3)
print(fib_series[-1])
