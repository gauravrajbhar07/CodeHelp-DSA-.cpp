# https://leetcode.com/problems/top-k-frequent-elements/description/

'''
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
'''

from collections import defaultdict

def top_k_frequent_elements(alist,k):
    
    # using hashmap
    res =[]
    dic = defaultdict(int)
    size = len(alist) + 1
    
    freq = [[] for i in range(size)]
    # [[], [], [], [], [], []]
    # print(freq)
    for i in alist:
        dic[i] = 1 + dic.get(i,0)
    print(dic.items())
    
    # Whenever we want to insert two valueswe can use .item() method
    # dict_items([(1, 3), (2, 2), (3, 1)])
    
    #
    for n ,c in dic.items():
        freq[c].append(n)
        
    res =[]
    for i in range(len(alist),0,-1):
        for n in freq[i]:
            res.append(n)
            if(len(res) == k):
                return res
        
    
    # print(res)
    
    
            
    return res
    
    
    
                    
            
            
    
    
    



alist = [1,1,1,2,2,3]
k = 2
print(top_k_frequent_elements(alist,k))