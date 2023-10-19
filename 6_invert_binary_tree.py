'''
Given the root of a binary tree, invert the tree, and return its root.

Inputs: 
- root: array 

Outputs: 
- inverted array: array
'''

def invert_binary_tree(root: list) -> list:
    len_root = len(root)
    new_list = [] 
    i = 0
    j = 1
    while root:
        temp_list = root[i:j]
        reverse_temp_list = temp_list[::-1]
        new_list.extend(reverse_temp_list)

        del root[i:j]
        j *= 2

    return new_list


if __name__=='__main__':
    root = [1, 3, 5, 4, 2, 8, 0] # [4, 2, 7, 1, 3, 6, 9]            # 
    print(invert_binary_tree(root=root))



# builtincolorado --> job searching