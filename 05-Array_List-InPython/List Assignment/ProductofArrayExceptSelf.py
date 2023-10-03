def productExceptSelf(nums):
    res = [1] * len(nums)
    # print([1] *len(nums))
    multi1 = 1
    for i in range(0,len(nums)):    
        res[i] = multi1
        multi1*=nums[i]
    # print(res)
    postfix = 1
    for i in range(len(res)-1,-1,-1):
        res[i] = postfix*res[i]
        postfix = postfix*nums[i]
        
        

    return res


        
    

print(productExceptSelf([-1,1,0,-3,3]))
