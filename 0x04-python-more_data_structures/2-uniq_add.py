#!/usr/bin/python3


def uniq_add(my_list=[]):

    result = 0
    for elem in set(my_list):
        result += elem
    return (result)
