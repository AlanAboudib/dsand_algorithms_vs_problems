"""
   Write-Up
   --------

   The solution to this problem in O(n) is so simple.

   Since we know that only 0s, 1s and 2s are allowed in the list to be sorted,
   we can just traverse this list one time and take each element and put it in 
   a separate list: so we put all zeros in one list, ones in another and twos
   in a third list.

   At the end we simple concatenate the three lists:
  
   [0,0,.] concat [1,1,...] concat [2,2,...]
"""

from collections import defaultdict

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """


    # define dictionary of lists
    # this dictionary has the following layout
    # lists[0] = [0,0,....]
    # lists[1] = [1,1,....]
    # lists[2] = [2,2,....]
    lists = defaultdict(list)

    # iterate in 'input_list' and add each element to the corresponding
    # list in 'lists'
    for elem in input_list:
        lists[elem].append(elem)

    # at this point, we have separated 0s, 1s and 2s into
    # three separate lists. All what we need to do now is to concatenate
    # the three lists to obtain a sorted list

    return lists[0] + lists[1] + lists[2]


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
