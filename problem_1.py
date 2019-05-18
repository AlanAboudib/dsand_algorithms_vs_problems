"""
   Write-Up
   --------
   I solve this problem by a divide and conquer approach.

   I start from the observation that the sqrt for a number > 1 can at most be equal
   to half of the number (sqrt(4) = 2). 

   So, I limit my search to the the integers in the interval [0, number /2]
   Within that interval, I apply a binary search with complexity of O(log(n))
   to find the solution using the fact that:

   if x > y => sqrt(x) > sqrt(y) for x, y in R+
"""

import math

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    # this is an easy case, the square root of 1
    if number == 1:
        return 1
    

    # fix a lower and a higher bound within which to look for a square root
    low = 0
    high = number

    # the tested square root will be always to the integer closest to the
    # middle point between 'high' and 'low'
    sqrt = math.floor((high - low) / 2)



    # sentinel values are if the 'sqrt' is an exact answer (the real square root)
    # sqrt * sqrt == number:
    # or if the whole integer space around the exact real square root has been tested
    # math.floor(high) - math.floor(low) = 1 or 0
    while math.floor(high) - math.floor(low) > 1 and sqrt * sqrt != number:

        # if 'sqrt' is larger than the squared root
        # search only in the space less than 'sqrt'
        # so 'high' is assigned 'sqrt'
        if sqrt * sqrt > number:
            high = sqrt            
            sqrt -= (high - low) / 2
            sqrt = math.floor(sqrt)

        # if 'sqrt' is smaller than the squared root
        # search only in the space high than 'sqrt'
        # so 'low' is assigned 'sqrt'
        else:
            low = sqrt            
            sqrt += (high - low) / 2
            sqrt = math.floor(sqrt)            


    # when the while loop exits, it meas that the answer is found
    return sqrt

print ("sqrt(9) = {}".format(sqrt(9)), "Pass" if  (3 == sqrt(9)) else "Fail")
print ("sqrt(0) = {}".format(sqrt(0)), "Pass" if  (0 == sqrt(0)) else "Fail")
print ("sqrt(16) = {}".format(sqrt(16)), "Pass" if  (4 == sqrt(16)) else "Fail")
print ("sqrt(1) = {}".format(sqrt(1)), "Pass" if  (1 == sqrt(1)) else "Fail")
print ("sqrt(27) = {}".format(sqrt(27)), "Pass" if  (5 == sqrt(27)) else "Fail")
print ("sqrt(36) = {}".format(sqrt(36)), "Pass" if  (6 == sqrt(36)) else "Fail")
print ("sqrt(39) = {}".format(sqrt(39)), "Pass" if  (6 == sqrt(39)) else "Fail")
print ("sqrt(12) = {}".format(sqrt(144)), "Pass" if  (12 == sqrt(144)) else "Fail")
print ("sqrt(12) = {}".format(sqrt(150)), "Pass" if  (12 == sqrt(150)) else "Fail")
