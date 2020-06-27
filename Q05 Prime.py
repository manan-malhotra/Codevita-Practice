num = int(input())
arr = []
sum = 0
count = 0
if num > 1:
    for i in range(2, num + 2):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            arr.append(i)


def is_prime(sum):
    for i in range(2, (sum // 2) + 2):
        if sum % i == 0:
            print(f"sum {sum}")
            return False
        else:
            return True


for i in range(0, len(arr)):
    sum = sum + arr[i]
    if sum <= num:
        if is_prime(sum):
            count = count + 1

print(count)

"""
Some prime numbers can be expressed as a sum of other consecutive prime numbers.
•	For example

o	5 = 2 + 3,
o	17 = 2 + 3 + 5 + 7,
o	41 = 2 + 3 + 5 + 7 + 11 + 13.
Your task is to find out how many prime numbers which satisfy this property are present in the range 3 to N subject to a constraint that summation should always start with number 2


S.no	Input	Output	Comment
1	20	2	(Below 20 there are two such members; 5 and 17) 5=2+3 17=2+3+65+7
2	15	1
"""
