"""
You are given the heads of two sorted linked lists `list1` and `list2`. 
Merge the two lists into one sorted list. The list should be made by splcing together the nodes of the first two lists.
Return the head of the merged linked list. 

Inputs: 
 - list1: array of numbers
 - list2: array of numbers 

Outputs: 
 - sorted array
"""

def merged_two_sorted_lists(list1: list, list2: list) -> list: 
    return sorted(list1 + list2)




if __name__ == '__main__':
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    print(merged_two_sorted_lists(list1=list1, list2=list2))