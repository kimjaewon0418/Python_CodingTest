import sys
input = sys.stdin.readline

n = int(input())
max = -1

for i in range(n):
    a,b,c = map(int, input().split())
    temp = 0
    if a==b==c:
        temp = 10000 + a*1000
    elif a==b or a==c or b==c:
        if a==b:
            temp = 1000 + a*100
        else:
            temp = 1000 + c*100
    else:
        temp = max(max(a,b),c)*100

    if max < temp:
        max = temp

print(max)