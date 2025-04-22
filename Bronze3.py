import sys

# sys.stdin.readline -> 정수 입력 가능
# sys.stdout.write -> 문자열 입력 가능

input = sys.stdin.readline()

while True:
    a,b,c = map(int, input.split())
    if a == b == c == 0:
        break
    if max(a,b,c) > a+b+c - max(a,b,c):
        print('Invalid')
    elif a == b or b==c or a==c:
        print('Isosceles')
    elif a == b == c:
        print('Equilateral')
    else:
        print('Scalene')
    break