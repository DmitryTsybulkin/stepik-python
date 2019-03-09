gen = input()
i = 0
x = 0
while i < len(gen):
    while (x < len (gen)) and (gen[i] == gen[x]):
        x +=1
    print(gen[i], x-i, sep='', end='')
    i = x