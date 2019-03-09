# put your python code here
import numpy as np

inp = int(input())

if -15 < inp <= 12 or 14 < inp < 17 or 19 <= inp < +np.inf:
    print(True)
else:
    print(False)
