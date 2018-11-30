#!/usr/bin/python3

import numpy as np

def merge2(list_of_intervalls):
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


def merge(list_of_intervalls):
    """
    Takes a list of tupels of integers and returns the a list where all the overlapping intervalls are merged.
    Would be possible with float which will be mapped to integers.
    """
    if (len(list_of_intervalls) == 0):                                          # check for Empty list and return one if given.
        return []
    if (len(list_of_intervalls) == 1):                                          # check for list with only one element and return it if given.
        return list_of_intervalls
    
    max_number, min_number= -2^63, 2^63 - 1                                     # initialisation with biggest or smallest number possible
    for kk in range(len(list_of_intervalls)):                                   # find smallest and greatest element
        if (list_of_intervalls[kk][0] < min_number):
            min_number = list_of_intervalls[kk][0]
        if (list_of_intervalls[kk][1] > max_number):
            max_number = list_of_intervalls[kk][1]
    np_array_of_intervalls = np.array(list_of_intervalls, dtype=int)
    start_end_array = np.zeros((2, max_number-min_number+1), dtype=int)         # Spans up an axis for start and and point via starting at the smalles element
    
    for ii in range(len(np_array_of_intervalls)):                               # Adds an counter to every point on the axis for each starting and ending intervall
        start_end_array[0, np_array_of_intervalls[ii,0] - min_number] += 1
        start_end_array[1, np_array_of_intervalls[ii,1] - min_number] += 1
    
    solution_array = np.array([], dtype = int)
    counter = 0
    for jj in range(max_number-min_number+1):
        counter -= start_end_array[1,jj]
        if (counter == 0):
            solution_array = np.append(solution_array,jj+min_number)
        counter += start_end_array[0,jj]
    
    solution_list = np.reshape(solution_array[:], (-1, 2)).tolist()
    return solution_list
    
    
