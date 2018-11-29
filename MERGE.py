#!/usr/bin/python3

import numpy as np

def merge(list_of_intervalls):
    """ 
    Takes a list of tupels which have to be sorted so that the smaler number of both is in the front.
    The function will sort the tupel first by the first element and as second key by the second element.
    The resulting list of intervalls will be merged if overlapping.
    """
    if (len(list_of_intervalls) == 0):                              # check for Empty list and return one if given.
        return []
    if (len(list_of_intervalls) == 1):
        return list_of_intervalls
    sorted_array = np.sort(np.array(list_of_intervalls),axis=0)     # sort the tupel first by the first and second by the second element
    solution_array = np.array([sorted_array[0,]])                   # The solution starts with the lowest interval
    for ii in range(1,len(sorted_array)):
        if (solution_array[-1,1] > sorted_array[ii,0]):             # If the next interval overlaps just update the bigger number
            solution_array[-1,1] =  sorted_array[ii,1]
        else:
            solution_array = np.vstack((solution_array[:,:],np.array([sorted_array[ii,:]])))     # If not overlapping add to solution interval
    return  solution_array.tolist()


