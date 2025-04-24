import sys
input = sys.stdin.readline

n = int(input())
sum = 0
count = 0
a = list(map(int, input().split()))
for i in range(n):
    if a[i] == 1:
        count = count+1
        sum = sum + count
    else:
        count = 0

print(sum)