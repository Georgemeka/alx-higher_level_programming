#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return my_list
    else:
        index = len(my_list) - 1
    for i in my_list:
        print("{:d}".format(my_list[index]))
        index -= 1
