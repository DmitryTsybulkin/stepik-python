# put your python code here
count = int(input())
a = 0
arr = []

for itr in range(count):
    line = str(itr) * itr
    while len(arr) != count:
        for it in line:
            arr.append(it)

for i in arr:
    print(i, end=' ')




