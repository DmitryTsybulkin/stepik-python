# put your python code here
# put your python code here
lst = list(input().split(' '))
x = int(input())
indexes = list()
i = 0
while i < len(lst):
    if int(lst[i]) == x:
        indexes.append(i)
    i += 1
if len(indexes) == 0:
    print('Отсутствует')
else:
    res = str()
    for i in indexes: res += str(i) + ' '
    print(res)




