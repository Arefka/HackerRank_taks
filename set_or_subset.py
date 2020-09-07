'''
===============================================================

You are given two sets, A and B.
Your job is to find whether set A is a subset of set B.

If set A is subset of set B, print True.
If set A is not a subset of set B, print False.

The first line will contain the number of test cases, T.
The first line of each test case contains the number of elements in set A.
The second line of each test case contains the space separated elements of set A.
The third line of each test case contains the number of elements in set B.
The fourth line of each test case contains the space separated elements of set B.

===============================================================
'''

cases_count = input()

for test_case in range(0, int(cases_count)):
    elements_count_set_A = input()
    set_A = set(input().split())
    elements_count_set_B = input()
    set_B = set(input().split())

    print(len(set_A.difference(set_B)) == 0)