# put your python code here
line = str(input())

start = int(line[0]) + int(line[1]) + int(line[2])
end = int(line[-1]) + int(line[-2]) + int(line[-3])

if start == end:
    print("Счастливый")
else:
    print("Обычный")



