a = [ int(i) for i in input().split() ]
if len(a) == 1:
    print(a[0])
else:
    print( ' '.join([ str ( a[j - 1] + a[j + 1] ) for j in range(len(a) - 1)] + [str(a[-2]+a[0])]))