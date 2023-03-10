#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    number_of_arg = len(argv) - 1

    if number_of_arg == 0:
        print("O arguments.")
    elif number_of_arg == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(number_of_arg))

        for i in range(number_of_arg):
            print('{}: {}'.format(i + 1, argv[i + 1]))
