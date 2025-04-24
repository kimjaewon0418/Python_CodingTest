import sys
input = sys.stdin.readline

n = int(input())
a = [0,1,0,0]
 
for i in range(n):
    x,y = map(int,input().split())
    temp = a[x]
    a[x] = a[y]
    a[y] = temp

for i in range(1,4):
    if a[i] ==1:
        print(i)
        break