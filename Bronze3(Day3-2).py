import sys
input = sys.stdin.readline

max = 0
now = 0
for i in range(10):
    a,b = map(int,input().split())
    now += b-a
    if now > max:
        max = now
print(max)


    
