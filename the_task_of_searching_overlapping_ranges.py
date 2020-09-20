'''
===============================================================

    In this speech I want to discuss about the task of searching overlapping ranges:

    We have some array of ranges, each range include a value of start point and a value of endpoint.
    And we should develop a function, which take an input array and return a count of overlapping ranges.

    For example, if we have an input array like this [[1,3], [3, 10], [9, 18]] our function should return 2,
    because we have two overlapping ranges [3, 10] and [9, 18].

    So, let's think about cases, which can we have if we are going to write our function:
    - the first case is about two consecutive overlapping sequences like this [1, 3] and [2, 4]. We can calculate
    a fact of inclusion start point of the second sequence in the first sequence. The same example is [2, 4] and [1, 3].
    - the second case is about situation, when one range is a sub-range of another. Something like this [4, 5] and [1, 9].
    In this case we should check start point and endpoint of each sequence to find a fact of inclusion it in another sequence.

    It's easy to imaging two this cases with classing segments in the OX system.

    But there is the third case like this [5, 9], [27, 6]. To my mind, it's not easy to understand - how can the range be minus.

    The main idea of the third case in thinking about a sequence as a clock dial. In this paradigm we are able to have a range like this [11, 4].
    And it's easy to imaging that ranges [9, 3] and [10, 2] or ranges [8, 4] and [10, 11] are overlapping ranges.

    On one hand we have a very useful paradigm of imaging a sequence as a clock dial. On another hand we have a
    problem of limit value of our clock dial. A classic clock dial has a 12 number as a limit value. But, if we try to
    use this paradigm in thinking about a year, we will have a 365 number as a limit value...

    Ok, we have no information about limit value of the sequence, but we should develop a universal algorithm. How can we do it?

    Why don't we define the limit value as a biggest value of input ranges.
    For example, if we are going to think about months and the biggest value in input ranges
    is 28 (elements of input array like this [20, 28], [3, 7], [5, 15]) - we can gas that our month can be a february.
    So, if the biggest value in input ranges in 31 (for example, [31, 5], [4, 10], [12, 15]) we can gas that our month
    can be the one of this months [January, March, May, July, August, October, December].


===============================================================
'''

