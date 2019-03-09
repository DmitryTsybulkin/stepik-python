# put your python code here
a = int(input())
b = int(input())
c = int(input())

if max(a, b, c) == a:
    print(a)
    if min(a, b, c) == b:
        print(b)
        print(c)
    elif min(a, b, c) == c:
        print(c)
        print(b)
elif max(a, b, c) == b:
    print(b)
    if min(a, b, c) == a:
        print(a)
        print(c)
    elif min(a, b, c) == c:
        print(c)
        print(a)
elif max(a, b, c) == c:
    print(c)
    if min(a, b, c) == a:
        print(a)
        print(b)
    elif min(a, b, c) == b:
        print(b)
        print(a)
