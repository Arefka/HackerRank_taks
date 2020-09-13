'''
===============================================================

    Mr. Vincent works in a door mat manufacturing company.
    One day, he designed a new door mat with the following specifications:

    Mat size must be X. ( is an odd natural number, and  is  times .)
    The design should have 'WELCOME' written in the center.
    The design pattern should only use |, . and - characters.
    Sample Designs

        Size: 7 x 21
        ---------.|.---------
        ------.|..|..|.------
        ---.|..|..|..|..|.---
        -------WELCOME-------
        ---.|..|..|..|..|.---
        ------.|..|..|.------
        ---------.|.---------

        Size: 11 x 33
        ---------------.|.---------------
        ------------.|..|..|.------------
        ---------.|..|..|..|..|.---------
        ------.|..|..|..|..|..|..|.------
        ---.|..|..|..|..|..|..|..|..|.---
        -------------WELCOME-------------
        ---.|..|..|..|..|..|..|..|..|.---
        ------.|..|..|..|..|..|..|.------
        ---------.|..|..|..|..|.---------
        ------------.|..|..|.------------
        ---------------.|.---------------
    Input Format: A single line containing the space separated values of N and M.
    Constraints: 5 < N < 101; 15 < M < 303.
    Output Format: Output the design pattern.

===============================================================
'''

def door_mat(n_value: int, m_value: int):
    middle_horizontally_point =  int(m_value / 2) + 1
    middle_vertically_point = int(n_value / 2) + 1

    for i in range(0, middle_vertically_point-1):
        dash_count = middle_horizontally_point - (i * 3) - 2
        print(('-' * dash_count) + ('.|.' * i) + '.|.' + ('.|.' * i) + ('-' * dash_count))

    print(('-' * (middle_horizontally_point - int(len('WELCOME')/2) - 1)) + 'WELCOME' + ('-' * (middle_horizontally_point - int(len('WELCOME')/2) - 1)))

    for i in range(0, middle_vertically_point-1):
        j = middle_vertically_point - 2 - i
        dash_count = middle_horizontally_point - (j * 3) - 2
        print(('-' * dash_count) + ('.|.' * j) + '.|.' + ('.|.' * j) + ('-' * dash_count))

def door_mat_second_variant(n_value: int, m_value: int):
    temple = [('.|.' * (2 * i + 1)).center(m_value, '-') for i in range(n_value // 2)]
    print('\n'.join(temple + ['WELCOME'.center(m_value, '-')] + temple[::-1]))

################# example: #################

first_example = [7, 21]
second_examle = [11, 33]

door_mat(first_example[0], first_example[1])
door_mat(second_examle[0], second_examle[1])

door_mat_second_variant(first_example[0], first_example[1])
door_mat_second_variant(second_examle[0], second_examle[1])