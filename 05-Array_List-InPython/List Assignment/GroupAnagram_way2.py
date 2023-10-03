
# https://leetcode.com/problems/group-anagrams/description/

'''
Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
'''


def groupAnagrams(strs):
    anagram = {}
    for word in strs:
        group_Key = ''.join(sorted(word))
        if group_Key not in anagram:
            anagram[group_Key] = [word]
        else:
            anagram[group_Key].extend([word])

    return anagram.values()
        
        
strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))