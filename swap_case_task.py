'''
===============================================================

    You are given a string and your task is to swap cases.
    In other words, convert all lowercase letters to uppercase letters and vice versa.

    Algorithmic complexity = O(n). n - input sentences length

===============================================================
'''

def char_swicher(item: str) -> str:
    if item.islower():
        return item.upper()
    return item.lower()

def swap_case(user_string: str) -> str:
    return ''.join([char_swicher(item) for item in user_string])

################# example: #################

first_case = ['Www.HackerRank.com', 'wWW.hACKERrANK.COM']
second_case = ['Pythonist 2', 'pYTHONIST 2']
print(swap_case(first_case[0]) == first_case[1])
print(swap_case(second_case[0]) == second_case[1])
