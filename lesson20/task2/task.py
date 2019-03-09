import sys

for i in sys.argv:
    if sys.argv.index(i) == 0:
        continue
    else:
        print(i)


