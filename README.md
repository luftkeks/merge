# merge
Merge Projekt for the Daimler TSS application.

The both scripts are written in Python 3.7.1 and with numpy 1.15.4.

the testMERGE.py script is simply for testing the "real" one.

The runtime of the merge2 function should be in order of the sorting algorithm wich is used by numpy. In the numpy documentary the worst case is given by and order of O(n\*log(n)). The runtime could also be improved by using a programming language which is closer to the hardware, such as C or Fortran.

The runtime of the merge function is in order of 2n+k where k beeing the highest value minus the lowest value plus one. If one wanted to use the faster function for floating point variables, a wrapping function has to be written, which maps all the floats to integers (e.g. by multipling them with 10^x to avoid decimals behind the point) and after the merging reversing the process.

It is assumend that the intervall array contains tupels where the smaller element comes first.

