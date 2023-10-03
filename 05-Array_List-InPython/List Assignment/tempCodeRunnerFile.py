# https://leetcode.com/problems/next-permutation/description/

'''
Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
'''

def next_permutation(nums):
    n = len(nums)
    i = 0
    lastInc = -1
    # lets find the last peek of the list
    while(i < n):
        if(nums[i]>nums[i-1]):
            lastInc = nums[i]
        i+=1


    if(lastInc == -1):
        l = 0
        r = len(nums)-1
        
        while(i <= r):
            nums[i],nums[r] = nums[r],nums[i]
            i+=1
            r-=1
        # return nums
        print(nums)
        return
    
    # find the element in the range of (nums[lastInc - 1] to nums[lastInc]) to the right
    # mn = nums[lastInc]
    index = lastInc
    
    for i in range(index,n,-1):
        if(nums[i] > nums[lastInc-1] and nums[i] < nums[index]) :
            index = i 
        
    nums[lastInc-1], nums[index-1] =nums[index-1] ,nums[lastInc-1]
    sorted(nums[lastInc:])
    
    while True:
        swapped = False
        for k in range(i, len(nums) - 1):
            if nums[k] > nums[k + 1]:
                swapped = True
                nums[k], nums[k + 1] = nums[k + 1], nums[k]
        if swapped == False: break
    
    return nums
            
            
        
    
    
    return nums
    
        
    # print(lastInc)
    
    
    
    
    
    
    
nums = [5,4,3,2,1]
print(next_permutation(nums))