#!/usr/bin/python3
def safe_print_list(my_list=None, x=0):
    if my_list is None:
        my_list = []
    a = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            a += 1
    except IndexError:
        y = None
    print()
    return a