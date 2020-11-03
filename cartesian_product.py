'''
===============================================================

    itertools.product()

    This tool computes the cartesian product of input iterables.
    It is equivalent to nested for-loops.
    For example, product(A, B) returns the same as ((x,y) for x in A for y in B).

===============================================================
'''
from itertools import product

def cartesian_product_calculation():
    a_elements = input().split()
    b_elements = input().split()
    a_num = [int(i) for i in a_elements]
    b_num = [int(i) for i in b_elements]
    answer = ' '.join([str(item) for item in list(product(a_num, b_num))])

    print(answer)