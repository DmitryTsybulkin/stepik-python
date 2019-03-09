x = [int(i) for i in input().split()]
x.sort()
i = 0
while i < len(x) - 1:
  if x[i] == x[i + 1]:
    print(x[i], ' ', end = '')
    i += x.count(x[i])    
  else:
    i += 1