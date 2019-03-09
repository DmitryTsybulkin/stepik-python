# put your python code here
line = str(input())

# 1,  - программист
# 2,3,4 - программиста
# 5,6,7,8,9,10, 11 - программистов

if line.endswith('11') or line.endswith('5') or line.endswith('6') \
        or line.endswith('7') or line.endswith('8') or line.endswith('9') \
        or line.endswith('10') or line.endswith('0') or line.endswith('12')\
        or line.endswith('13') or line.endswith('14'):
    print(line + ' программистов')
elif line.endswith('1'):
    print(line + ' программист')
elif line.endswith('2') or line.endswith('3') or line.endswith('4'):
    print(line + ' программиста')
