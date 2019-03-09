# put your python code here
s = int(input())
summat = 0
arr = [s]
while s != 0:
    a = int(input())
    s += a
    arr.append(a)
for i in arr:
    summat += (i ** 2)
print(summat)



