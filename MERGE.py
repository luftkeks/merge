#!/usr/bin/python3

import numpy as np

def merge2(list_of_intervalls):
    """ 
    Takes a list of tupels which have to be sorted so that the smaler number of both is in the front.
    The function will sort the tupel first by the first element and as second key by the second element.
    The resulting list of intervalls will be merged if overlapping.
    """
    if (len(list_of_intervalls) == 0):                              # Check for Empty list and return one if given.
        return []
    if (len(list_of_intervalls) == 1):
        return list_of_intervalls
    sorted_array = np.sort(np.array(list_of_intervalls),axis=0)     # Sort the tupel first by the first and second by the second element.
    solution_array = np.array([sorted_array[0,]])                   # The solution starts with the lowest interval.
    for ii in range(1,len(sorted_array)):
        if (solution_array[-1,1] > sorted_array[ii,0]):             # If the next interval overlaps just update the bigger number.
            solution_array[-1,1] =  sorted_array[ii,1]
        else:
            solution_array = np.vstack((solution_array[:,:],np.array([sorted_array[ii,:]])))     # If not overlapping add to solution interval.
    return  solution_array.tolist()


def merge(list_of_intervalls):
    """
    Takes a list of tupels of integers and returns the a list where all the overlapping intervalls are merged.
    Don't use this function with anything else than integers!
    """
    if (len(list_of_intervalls) == 0):                                          # Check for Empty list and return one if given.
        return []
    if (len(list_of_intervalls) == 1):                                          # Check for list with only one element and return it if given.
        return list_of_intervalls
    
    max_number, min_number= -2^63, 2^63 - 1                                     # Initialisation with biggest or smallest number possible.
    for kk in range(len(list_of_intervalls)):                                   # Find smallest and greatest element.
        if (list_of_intervalls[kk][0] < min_number):
            min_number = list_of_intervalls[kk][0]
        if (list_of_intervalls[kk][1] > max_number):
            max_number = list_of_intervalls[kk][1]
    np_array_of_intervalls = np.array(list_of_intervalls, dtype=int)
    start_end_array = np.zeros((2, max_number-min_number+1), dtype=int)         # Spans up an axis for start and and point via starting at the smalles element.
    
    for ii in range(len(np_array_of_intervalls)):                               # Adds one to a counter for every point on the axis 
        start_end_array[0, np_array_of_intervalls[ii,0] - min_number] += 1      # for each starting 
        start_end_array[1, np_array_of_intervalls[ii,1] - min_number] += 1      # and ending interval.
    
    solution_array = np.array([], dtype = int)                                  # Start the solution array, it will be wrapped to tupels at the end.
    counter = 0                                                                 # Creation of a counter to track whether an inteval is open.
    for jj in range(max_number-min_number+1):
        counter -= start_end_array[1,jj]                                        # Substract one for each closing interval at this position
        if (counter == 0) and not (start_end_array[1,jj] == 0):                 # If all intervals were closed this step, add the position to the solution_array.    
            solution_array = np.append(solution_array,jj+min_number)
        if (counter == 0) and not (start_end_array[0,jj] == 0):                 # If an initial interval was opended this step, add the position to the solution_array.
            solution_array = np.append(solution_array,jj+min_number)
        counter += start_end_array[0,jj]                                        # Add one to the counter for each opening interval at this position.
    solution_list = np.reshape(solution_array[:], (-1, 2)).tolist()             # Wrap the array of integers to their intervals and store it in a list
    return solution_list
    
    
