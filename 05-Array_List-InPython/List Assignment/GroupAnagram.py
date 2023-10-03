
  
from collections import defaultdict
  
  
def merger(alist):
    strs = ""
    a= []
    for i in alist:
        strs = strs + i
    # print(strs) 
    # a.append(strs)
    return strs

def groupAnagram(strs):
    
    strs.sort()
    checkArr= []
    for i in strs:
    # k = sorted(i)
        k = ''.join(sorted(i))
        if(k not in checkArr):
            checkArr.append(k)
    
    
    res =[]
    for i in checkArr:
        r = []
        k = sorted(i)
        for j in range(0,len(strs)):
            l = strs[j]
            # print(l)
            r_val = ''.join(l)
            if(sorted(strs[j]) == k):
                r.append(r_val)
        res.append(r)

    return res


def groupAnagramOptimim(strs):
    
    # hashMap
    res = defaultdict(list) #mapping character count to a list of anagram
    
    
    for i in strs:
        
        count =[0]*26  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        
        for j in i:
            count[ord(j) - ord("a")] += 1 
            # ord return ans asici value of a letter and we do to 
        
        res[tuple(count)].append(i)
        # list count can't be hashable in python thats why we use tuple 
    print(res)
    return res.values()
        
        
        
        
    
        
    
    
    
    return count


























strs =["eat","tea","tan","ate","nat","bat"]

print(groupAnagramOptimim(strs))


