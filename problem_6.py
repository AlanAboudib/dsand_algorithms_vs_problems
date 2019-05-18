"""
   Write-Up
   --------
   It is easy to compute the min and max of an unsorted array in a single traversal O(n)

   We intialize two variables that hold the min and max values

   then we take each element from the array and we update the 'min' variable by
   assigning the list element to it if the latter is lower. 

   We do the same for the 'max' variable by checking out if the list element we
   took is higher and then assigning it to the 'max' variable if it is the case.


"""

def get_min_max_by_sorting(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """

    # initialize the min and max to None
    mn = None
    mx = None

    # start traversing the list
    for i in ints:

        # intialize the mn and max values
        if mn is None:
            mn = i
            
        if mx is None:
            mx = i

        # now update the min and max values by comparing with the last stored value
        mn = i if i < mn else mn
        mx = i if i > mx else mx

    return mn, mx

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max_by_sorting(l)) else "Fail")
