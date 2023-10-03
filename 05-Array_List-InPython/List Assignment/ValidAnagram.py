# https://leetcode.com/problems/valid-anagram/description/

'''
Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 '''


def isAnagram(s,t):
    # This will give us a time complexity of big O of N 
    # but this space complexity is big 0 of s+t 
    
    

    if(len(s) != len(t)):
        return False
        
    countS,countT = {},{}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i],0)
        countT[t[i]] = 1 + countT.get(t[i],0)


    for i in countS:
        if(countS[i] != countT.get(i,0)):
            return False
    return True


def BetterTCisAnagram(s,t):
   return sorted(s) == sorted(t)
    # If they both are sorted then they must have equal same elements that means they are in a anagram
    # this will give a better space complexity and the time complexity is N log N


s = "anagram"
t = "nagaram"
print(BetterTCisAnagram(s,t))