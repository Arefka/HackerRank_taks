import numpy
'''
===============================================================

    You are given a 2-D array with dimensions N*M.
    Your task is to perform the SUM tool over axis 0 and then find the PROD of that result.

    Compute the sum along axis 0. Then, print the product of that sum.

===============================================================
'''
numpy.set_printoptions(precision=1)

def numpy_fun(matrix_values: list):
    my_array = numpy.array(matrix_values)
    sum_array = numpy.sum(my_array, axis=0)
    prod_array = numpy.prod(sum_array)
    return prod_array

def numpy_min(matrix_values: list):
    print(numpy.min(matrix_values, axis=0))
    print(numpy.min(matrix_values, axis=1))
    print(numpy.min(matrix_values, axis=None))
    print(numpy.min(matrix_values))

def numpy_max(matrix_values: list):
    print(numpy.max(matrix_values, axis=0))
    print(numpy.max(matrix_values, axis=1))
    print(numpy.max(matrix_values, axis=None))
    print(numpy.max(matrix_values))

def numpy_mean(matrix_values: list):
    print(numpy.mean(matrix_values, axis=0))
    print(numpy.mean(matrix_values, axis=1))
    print(numpy.mean(matrix_values, axis=None))
    print(numpy.mean(matrix_values))

def numpy_var(matrix_values: list):
    print(numpy.var(matrix_values, axis=0))
    print(numpy.var(matrix_values, axis=1))
    print(numpy.var(matrix_values, axis=None))
    print(numpy.var(matrix_values))

def numpy_std(matrix_values: list):
    print(numpy.std(matrix_values, axis=0))
    print(numpy.std(matrix_values, axis=1))
    print(numpy.std(matrix_values, axis=None))
    print(numpy.std(matrix_values))

def numpy_dot_cross(first_list: list, second_list: list):
    print(numpy.dot(first_list, second_list))
    print(numpy.cross(first_list, second_list))

def numpy_inner_outer(first_list: list, second_list: list):
    print(numpy.inner(first_list, second_list))
    print(numpy.outer(first_list, second_list))

################# example: #################

examples_list = [[1, 2], [3, 4]]
#print(numpy_fun(examples_list))
#numpy_dot_cross(examples_list[0], examples_list[1])
numpy_inner_outer(examples_list[0], examples_list[1])