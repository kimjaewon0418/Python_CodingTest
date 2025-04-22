import sys
input = sys.stdin.readline

n = int(input())
sum = 0
for i in range(n):
    sum = sum + int(input())
print(sum - (n-1))