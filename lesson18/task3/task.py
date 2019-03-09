def modify_list(l):
    # put your python code here
    for i in l:
        if i % 2 == 0:
            i /= 2
        elif i % 2 > 0:
            l.remove(i)
