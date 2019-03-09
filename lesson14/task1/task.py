# put your python code here

a = int(input())
b = int(input())
c = int(input())
d = int(input())

for i in range(c, d+1):
    print('\t', str(i), end='')

for it in range(a, b+1):
    print('')
    print(it, end='\t')
    for itr in range(c, d+1):
        print(str(it*itr), end='\t')
