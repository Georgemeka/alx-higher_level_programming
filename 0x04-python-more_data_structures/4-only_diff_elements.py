#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    diff = set_1 - set_2
    diff2 = set_2 - set_1

    unique_elements = diff.union(diff2)
    return unique_elements
