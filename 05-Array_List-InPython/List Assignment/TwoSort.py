# https://leetcode.com/problems/two-sum/description/

'''
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

'''



# l = len(nums)

# for i in range(l):
    
#     for j in range(i+1,l):
#         if(nums[i] + nums[j] == target):
#             res.append(i)
#             res.append(j)
#             break
def TwoSum(nums,target):
    prevMap = {} # index:value
    for i,n in enumerate(nums):
        diff = target - n
        # print(diff)
        if( diff in prevMap):
            return [prevMap[diff],i]
        prevMap[n] = i
    return
        

# print(res)



nums = [3,2,3]
target = 6
print(TwoSum(nums,target))