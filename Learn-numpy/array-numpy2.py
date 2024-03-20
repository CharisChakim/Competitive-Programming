import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    array =  numpy.array(arr, float)[::-1]
    return array

arr = input().strip().split(' ')