'''
===============================================================

    You are given an integer, N.
    Your task is to print an alphabet rangoli of size N.
    (Rangoli is a form of Indian folk art based on creation of patterns.)

    Different sizes of alphabet rangoli are shown below:

    #size 3
        ----c----
        --c-b-c--
        c-b-a-b-c
        --c-b-c--
        ----c----

    #size 5
        --------e--------
        ------e-d-e------
        ----e-d-c-d-e----
        --e-d-c-b-c-d-e--
        e-d-c-b-a-b-c-d-e
        --e-d-c-b-c-d-e--
        ----e-d-c-d-e----
        ------e-d-e------
        --------e--------

===============================================================
'''

def print_rangoli(size):
    symbols_dict = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m',
                    14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}
    line_part = []
    for i in range(0, size):
        line_part.append([])
        for j in range(i, size):
            symb = symbols_dict[j+1]
            if j+1 < size:
                symb += '-'
            line_part[i].append(symb)
        for n in range(0, size - len(line_part[i])):
            symb = '--'
            line_part[i].append(symb)
    for i in range(0, len(line_part)):
        j = len(line_part) - 1 - i
        line = ''.join(line_part[j][::-1][::-1])
        print(''.join(reversed(line)) + line[1:])
    for i in range(1, len(line_part)):
        line = ''.join(line_part[i][:])
        print(''.join(reversed(line)) + line[1:])


################# example: #################

print_rangoli(3)
#print_rangoli(5)
#print_rangoli(7)