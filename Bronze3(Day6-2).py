import sys
input  = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

y = 0
m = 0

for i in range(n):
    y += 10
    m += 15
    time = a[i]

    y += time // 30 * 10
    m += time // 60 * 15

if y == m:
    print("y m", str(y))
elif y < m:
    print('y', str(y))
else:
    print('m', str(m))