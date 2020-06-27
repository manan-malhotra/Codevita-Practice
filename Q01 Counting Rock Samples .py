samples, ranges = [int(i) for i in input().split()]
count = 0
final = []
arr = list(map(int, input().split()))
for i in range(0, ranges):
    range1, range2 = [int(i) for i in input().split()]
    for j in range(0, samples):
        if range1 <= arr[j] <= range2:
            count = count + 1
    final.append(count)
    count = 0
for i in range(0, len(final)):
    print(final[i], end=" ")

'''
Input Format: An positive integer S (the number of rock samples) separated by a blank space, and a positive integer R (the number of ranges of the laboratory); A list of the sizes of S samples (in ppm), as positive integers separated by space R lines where the ith line containing two positive integers, space separated, indicating the minimum size and maximum size respectively of the ith range.
Output Format: R lines where the ith line contains a single non-negative integer indicating the number of the samples which lie in the ith range.
Constraints:
•	10 <= S <= 10000
•	1 <= R <= 1000000
•	1<=size of Sample <= 1000
Example 1
•	Input: 10 2
•	345 604 321 433 704 470 808 718 517 811
•	300 350
•	400 700
Output: 2 4
Explanation:
There are 10 samples (S) and 2 ranges ( R ). The samples are 345, 604,811. The ranges are 300-350 and 400-700. There are 2 samples in the first range (345 and 321) and 4 samples in the second range (604, 433, 470, 517). Hence the two lines of the output are 2 and 4
'''
