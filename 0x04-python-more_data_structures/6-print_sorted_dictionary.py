#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorter = sorted(a_dictionary.keys())

    for keys in sorter:
        print("{}: {}".format(keys, a_dictionary.get(keys)))
