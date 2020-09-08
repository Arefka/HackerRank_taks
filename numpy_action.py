import numpy
'''
===============================================================

    You are given a 2-D array with dimensions N*M.
    Your task is to perform the SUM tool over axis 0 and then find the PROD of that result.

    Compute the sum along axis 0. Then, print the product of that sum.

===============================================================
'''

def numpy_fun(matrix_values: list):
    my_array = numpy.array(matrix_values)
    sum_array = numpy.sum(my_array, axis=0)
    prod_array = numpy.prod(sum_array)
    return prod_array

################# example: #################

examples_list = [[1, 2], [3, 4]]
print(numpy_fun(examples_list))

