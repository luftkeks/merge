#!/usr/bin/python3

import numpy as np

def merge(list_of_intervalls):
    """ 
    Takes a list of tupels which have to be sorted so that the smaler number of both is in the front.
    The funktion will sort the tupel first by the first element and as second key by the second element.
    Now it will call compare function for each unchecked tupel and thus jumping over checked tupel.
    """
    sorted_array_of_intervalls = np.sort(np.array(list_of_intervalls),axis=0)
    ii,jj = 0,0
    solution_array_of_intervalls = []
    return_tupel = [0,0]
    while ii < (len(sorted_array_of_intervalls)):
        return_tupel, jj = compare(sorted_array_of_intervalls[ii:,:])
        ii = ii + jj
        solution_array_of_intervalls.append(return_tupel)
    return  solution_array_of_intervalls

def compare(list_of_tupel):
    """
    Returns the longest interval starting with the lowest tupel by checking for overlapping intervals
    and the number of intervals which are merged. If only one element is given, the element is returned. 
    """
    lower_tupel = list_of_tupel[0,:]
    list_of_higher_tupel = list_of_tupel[1:,:]
    return_tupel=[lower_tupel[0],lower_tupel[1]]
    for ii in range(len(list_of_higher_tupel)):
        if return_tupel[1] > list_of_higher_tupel[ii,0]:
            return_tupel[1] = list_of_higher_tupel[ii,1]
        else:
            return (return_tupel, ii+1)
    return (return_tupel, 2)


if __name__ == "__main__":
	blub=[[25,30],[2,9],[39,41],[35,40],[14, 23],[4,8], [14,21], [14,22], [2,3] , [30,31], [-1,1],[1.4,1.8]]
	print(blub)
	print(merge(blub))
