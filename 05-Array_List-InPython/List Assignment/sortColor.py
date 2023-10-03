# https://leetcode.com/problems/sort-colors/description/

'''
Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]

'''

def sortColor(alist):

    low = 0 
    mid = 0
    high = len(alist) - 1

    while(mid <= high):
        if(alist[mid] == 0):
            alist[mid],alist[low] = alist[low],alist[mid]
            mid+=1
            low+=1
        elif(alist[mid] == 1):
            mid+=1
        else:
            alist[mid],alist[high] = alist[high],alist[mid]
            high-=1

    # return alist

alist = [2,0,2,1,1,0]
sortColor(alist)
print(alist)

