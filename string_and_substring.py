'''
===============================================================

    In this challenge, the user enters a string and a substring.
    You have to print the number of times that the substring occurs in the given string.
    String traversal will take place from left to right, not from right to left.

===============================================================
'''

def count_substring(string, sub_string):
    counter = 0
    num = 0
    while (num <= len(string)-len(sub_string)):
        if string[num:num+len(sub_string)] == sub_string:
            counter += 1
        num += 1
    return counter

################# example: #################

first_example = ['ABCDCDC', 'CDC']
second_example = ['mtr4 tpmtrmtrp r42Zmt', 'mtr']
print(count_substring(first_example[0], first_example[1]) == 2)
print(count_substring(second_example[0], second_example[1]) == 3)