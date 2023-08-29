#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Display a specified number, 'x', of elements from a provided list.

Parameters:
my_list (list): The source list containing elements to be displayed.
x (int): The count of elements from 'my_list' to be printed.

Returns:
The count of elements that were successfully printed
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
