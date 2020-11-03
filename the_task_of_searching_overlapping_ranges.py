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

    It's easy to imaging two this cases with classic segments in the OX system.

    But there is the third case like this [5, 9], [27, 6]. To my mind, it's not easy to understand - how can the range be minus.

    The main idea of the third case in thinking about a sequence as a clock dial. In this paradigm we are able to have a range like this [11, 4].
    And it's easy to imaging that ranges [9, 3] and [10, 2] or ranges [8, 4] and [10, 11] are overlapping ranges.

    On one hand we have a very useful paradigm of imaging a sequence as a clock dial. On another hand we have a
    problem of limit value of our clock dial. A classic clock dial has a 12 number as a limit value. But, if we try to
    use this paradigm in thinking about a year, we will have a 365 number as a limit value...

    Ok, we have no information about limit value of the sequence, but we should develop a universal algorithm. How can we do it?

    Why don't we define the limit value as a biggest value of input ranges?
    For example, if we are going to think about months and the biggest value of input ranges
    is 28 (elements of input array like this [20, 28], [3, 7], [5, 15]) - we can guess  that our month can be a february.
    So, if the biggest value of input ranges is 31 (for example, [31, 5], [4, 10], [12, 15]) we can guess that our month
    can be the one of this months [January, March, May, July, August, October, December].
    And if the biggest value of input ranges is 15 - so let's imaging some entity with diapason from 1 to 15 number.

    So, our function should be able to do this actions:
    - it takes input ranges array and find the biggest value;
    - it takes from each range it's item values;
    - it calculates the count of overlapping ranges.

    In pseudocode it can be something like this:
    our_function(input_array: array) {
        int N = 0;
        list_of_ranges_sets = new list();
        results_count_set = new set();

        // let's find the biggest value:
        for (each_range in input_array) do {
            if start_point > N then N = start_point
            if endpoint > N then N = endpoint
        }

        // let's create a list of ranges sets:
        for (each_range in input_array) do {
            if (start_point <= endpoint) then {
                // this is a case like [1, 10]
                for (item in range(start_point, endpoint)) do {
                    list_of_ranges_sets[each_range].Add(item);
                }
            }
            else {
                // this is a case like [25, 10]
                for (item in range(endpoint, N)) do {
                    list_of_ranges_sets[each_range].Add(item);
                }
                for (item in range(1, start_point)) do {
                    list_of_ranges_sets[each_range].Add(item);
                }
            }
        }

        // let's calculate the count of overlapping ranges:
        for (first_counter in range(0, len(list_of_ranges_sets)) do {
            for (second_counter in range(first_counter, len(list_of_ranges_sets))) do {
                first = list_of_ranges_sets[first_counter]
                second = list_of_ranges_sets[second_counter]
                if (len(intersection_of _sets(first, second)) > 0) then {
                    results_count_set.Add(first)
                    results_count_set.Add(second)
                }
            }
        }

        return len(results_count_set)
    }

===============================================================
'''

def count_overlapping_ranges(ranges_list: list) -> int:
    biggest_value = 1
    list_of_ranges_sets = []
    overlapping_list = []

    for each_range in ranges_list:
        if each_range[0] > biggest_value:
            biggest_value = each_range[0]
        if each_range[1] > biggest_value:
            biggest_value = each_range[1]

    for each_range in ranges_list:
        if (each_range[0] <= each_range[1]):
            list_of_ranges_sets.append(set())
            for number in range(each_range[0], each_range[1] + 1):
                list_of_ranges_sets[len(list_of_ranges_sets) - 1].add(number)
        else:
            list_of_ranges_sets.append(set())
            for number in range(1, each_range[1]+1):
                list_of_ranges_sets[len(list_of_ranges_sets) - 1].add(number)
            for number in range(each_range[0], biggest_value + 1):
                list_of_ranges_sets[len(list_of_ranges_sets) - 1].add(number)

    for num in range(len(list_of_ranges_sets) - 1):
        for item in list_of_ranges_sets[num + 1:]:
            if len(list_of_ranges_sets[num].intersection(item)) > 0:
                if list_of_ranges_sets[num] not in overlapping_list:
                    overlapping_list.append(list_of_ranges_sets[num])
                if item not in overlapping_list:
                    overlapping_list.append(item)

    return len(overlapping_list)

################# example: #################

first_ranges_list = [[3, 5], [6, 9], [8, 15], [16, 2], [18, 2]]
#second_range_list = [[10, 15], [14, 20], [1, 5]]
#third_range_list = [[1, 5], [12, 20], [10, 22], [21, 25]]
print(count_overlapping_ranges(first_ranges_list))
#print(count_overlapping_ranges(second_range_list))
#print(count_overlapping_ranges(third_range_list))
