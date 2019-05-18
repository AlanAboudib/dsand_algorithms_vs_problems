"""
   Write-UP
   --------

   The program takes a list of integers in the range [0,9], and rearrange its digits into two integers
   whose sum is maximal. In order to come up with a solution with a time complexity O(n.log(n)), 

   I first implement the merge sort algorithm tha thas an average (and worse case) complexities of O(n.log(n)).
   Then, I used the merge sort to sort the input list in ascending order. 

   Then, once the list is sorted, for instance [2,4,5,6,7], I iterate in reverse order only one time through
   this list: I first take 7 and put it in a list [7] then I take the 6 and put it in a second list [6],
   then the 5 in the first list [7,5], then the 4 in the second [6,4], etc..
   Iterating this list is O(n).

   By concatenating the contents of each list, I obtained the solution as two integers.
 
   the final complexity is O(n + n.log(n)) which is eqal to O(n (1 +log(n))) = O(nlog(n))

   
"""

def fusion(list1, list2):
    """
       merges to sorted lists. supposing that the lists are in ascending order

    """

    merged_list = []

    # the size of the lists
    s1 = len(list1)
    s2 = len(list2)

    # pointers to walk through the lists
    p1 = 0
    p2 = 0
    
    # loop while both pointers are still within the lists ranges
    while p1 < s1 and p2 < s2:

        # take the smallest element from each list
        e1 = list1[p1]
        e2 = list2[p2]    
        
        # add the smallest element first
        if e1 < e2:
            
            merged_list.append(e1)
            p1 += 1
            
        else:
            merged_list.append(e2)
            p2 += 1


    # now that the loop has terminated, it is possible that one of the
    # lists is not yet completely merged.
    # this can happen when list1 and list2 do not have the same size
    # in this case, I should just add the rest of the unfinished
    # list to the merged_list
    if p1 < s1:
        merged_list.extend(list1[p1:])

    if p2 < s2:
        merged_list.extend(list2[p2:])

    return merged_list




def merge_sort(lst):
    """
       sort the list 'lst' in ascending order using merge sort in O(nlog(n))
    """

    ## if the list has only one element return it as is
    if len(lst) == 1:
        return lst

    ## if the list has two elements, sort is so quick
    if len(lst) == 2:
        if lst[0] <= lst[1]:
            return lst
        else:
            return lst[::-1]
        
    ## we need to split the list into two lists with almost equal size

    # take the index of the middle element of the list
    mid_idx = len(lst) // 2

    # recursively sort each part
    list1 = merge_sort(lst[0:mid_idx])
    list2 = merge_sort(lst[mid_idx:])

    # now merge (fuse) the two sorted parts
    merged_list = fusion(list1, list2)

    return merged_list

    
def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    ## first I sort the list in O(n.log(n)) time using merge sort
    input_list = merge_sort(input_list)

    # then, I initialize two lists to hold the two number that will be summed
    num1_lst = []
    num2_lst = []

    # now we alternatively populate the above two lists
    # starting from the largest element in the sorted input_list
    for i in range(len(input_list) - 1, -1, -2):

        # add the current largest element to the first list
        num1_lst.append(str(input_list[i]))

        # add the following largest element to the second list
        if i - 1 >= 0:
            num2_lst.append(str(input_list[i-1]))


    # convert each list to a string by concatenating its
    # digits, and then to an in
    num1 = int(''.join(num1_lst))
    num2 = int(''.join(num2_lst))

    return [num1, num2]

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)



