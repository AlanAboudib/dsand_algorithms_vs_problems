"""
   Write-Up
   --------
   The way I accomplish this element search problem in the rotated sorted list is by
   using a divide-and-conquer approach.

   I start from the observation that if I divide a rotated sorted list into two lists
   without any overlapping elements, at least one of the resulting splits would be a
   sorted unrotated list. Here is and example: [5,6,7,8,,9,1,2,3,4]  can be split into
   [5,6,7,8] and [9,1,2,3,4]. the left one is sorted unrotated. The element is necessarily
   in one and only one of these lists. It is easy to know in each split I should search
   by only looking at the unrotated list. If the searched element smaller or equal  the last
   element and larger or equal to first element (in case of ascending order, the inverse for
   descending order), then we should exclude the rotated list and look only in the sorted one.
   Otherwise, we exclude the unrotated one and search only in the rotated part.

   For searching in the sorted one, I apply a binary search with complexity of O(log(n)).
   For searching the rotated part, I apply again the rotated/unrotated split recursively.
 
   Since I am  dividing the list by two each time and search in only one half, then I have
   a complexity of O(log(n))

   Note:

   there are some extreme cases where splitting results in two sorted, unrotated lists 
   ( when the whole list is unrotated), my code detects this and performs a binary
   seach on the whole list.

"""
def binary_search(input_list, number, low = None, high = None):
    """
       Find the index in the sorted (unrotated) input_list using recurrent calls
    """

    # low and high are the start and end indexes of 'input_list'
    # between which we are looking for a solution
    if low is None:
        low = 0

    if high is None:
        high = len(input_list) - 1


    # check whether the list is sorted in ascending of descending order

    # ascending
    if input_list[low] < input_list[high]:
        ascending = +1
    else:
        ascending = -1
        
    # stopping condition
    if low == high and input_list[low] == number:
        return low
    elif low == high and input_list[low] != number:
        return -1

    # the current search index
    index = (high - low) // 2 + low
    
    # check out the position of the number compared to the searched index
    # taking the sort type into acount
    if input_list[index] == number:
        return index
    
    elif ascending * number > ascending * input_list[index]:
        low = index + 1
    else:
        high = index - 1 if index - 1 > 0 else 0

    # get the answer
    index = binary_search(input_list, number, low = low, high = high)

    return index

    
    
def rotated_array_search(input_list, number, low = None, high = None):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    if low is None:
        low = 0

    if high is None:
        high = len(input_list) - 1


    # if the list is empty return -1
    if len(input_list) == 0:
        return -1

    if len(input_list) == 1:
        if input_list[0] == number:
            return 0
        else:
            return -1
        
    # if the list is of size two, then it is considered as unrotated
    if len(input_list[low:high + 1]) == 2:
        index = binary_search(input_list, number)
        return index

    # if we cut the list into two lists, we will be sure that
    # one of them is sorted and not rotated. This allows us
    # to quickly exclude one of the lists and search in the other one

    # get the middle index
    mid_idx = (high - low) // 2 + low

    # get the start and end element index of the two splits of input_list
    s1_start = low
    s1_end = mid_idx - 1

    s2_start = mid_idx
    s2_end = high

    # now compute the difference between elements correponding to each of
    #those indexes with the mid_idx
    # this can help us detect which split is rotated
    s1_start_diff = input_list[(s1_start - 1) % len(input_list)] - input_list[mid_idx]
    s1_end_diff = input_list[s1_end] - input_list[mid_idx]

    s2_start_diff = input_list[s2_start + 1] - input_list[mid_idx]
    s2_end_diff = input_list[(s2_end + 1) % len(input_list)] - input_list[mid_idx]
    
    # those are the two conditions that indicate a rotated list
    if s1_start_diff * s1_end_diff < 0 or abs(s1_end_diff) > abs(s1_start_diff):

        # the fact that we entered this if statement means that the second split
        # is sorted and unrotated, so let's check if the solution is in it
        if number <= max(input_list[s2_start + 1], input_list[s2_end]) and \
           number >= min(input_list[s2_start + 1], input_list[s2_end]):

            # apply classical binary search to find the index of the number
            index = binary_search(input_list, number, low = s2_start + 1, high = s2_end)

        # else, the number is in the unrotate list
        else:
            
            # get the results by recurrence
            index = rotated_array_search(input_list, number, low = s1_start, high = mid_idx )

    # else, if the rotated list is the second split
    elif s2_start_diff * s2_end_diff < 0 or abs(s2_start_diff) > abs(s2_end_diff):

        if number <= max(input_list[s1_start], input_list[s1_end]) and \
           number >= min(input_list[s1_start], input_list[s1_end]):

            index = binary_search(input_list, number, low = s1_start, high = s1_end)
            
        else:

            index = rotated_array_search(input_list, number, low = s2_start, high = s2_end)

    # in this case the whole list is not rotated
    else:

        index = binary_search(input_list, number)
        
    # return the final result
    return index

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 10])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 10])
test_function([[6, 7, 8], 8])
test_function([[6, 7, 5], 6])
test_function([[6, 7], 8])
test_function([[6, 7], 5])
test_function([[8, 7], 7])
test_function([[8], 9])
test_function([[], 9])

