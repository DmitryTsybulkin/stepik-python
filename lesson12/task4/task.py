# put your python code here
a = int(input())
b = int(input())

# and
i = 1
if a == b:
    print(a)
else:
    while True:
        if i // a > 0 and i % a == 0 and i // b > 0 and i % b == 0:
            print(i)
            break
        else:
            i += 1
