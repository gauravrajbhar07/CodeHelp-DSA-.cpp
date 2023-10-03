# https://leetcode.com/problems/contains-duplicate/description/

'''
Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''

def contains_duplicate(alist):
    
    seen =set()
    for i in alist:
        if(i in seen):
            return True
        seen.add(i)

    return False

    
        

    return False


alist = [1,1,1,3,3,4,3,2,4,2]
print(contains_duplicate(alist))
