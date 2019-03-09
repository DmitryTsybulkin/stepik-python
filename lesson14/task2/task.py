# put your python code here

a = int(input())
b = int(input())
s = 0
count = 0
for i in range(a, b+1):
    if i % 3 == 0:
        s += i
        count += 1
print(str(s / count))
