# Input : 
# lst1 = [23, 15, 2, 14, 14, 16, 20 ,52]
# lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
# Output :
# [23, 15, 2, 14, 14, 16, 20, 52, 2, 48, 
# 15, 12, 26, 32, 47, 54]

def union(l1,l2):

    ans =[]
   
    ans = l1 + l2

    return ans



# Maintained repetition and order
# Input : 
# lst1 = [23, 15, 2, 14, 14, 16, 20 ,52]
# lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
# Output :
# [2, 2, 12, 14, 14, 15, 15, 16, 20, 23, 
# 26, 32, 47, 48, 52, 54]



def MaintainedRepetitionAndOrder(l1,l2):
    ans =[]
   
    ans = l1 + l2
    ans.sort()

    return ans


lst1 = [23, 15, 2, 14, 14, 16, 20 ,52]
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]

print(union(lst1,lst2))

print(MaintainedRepetitionAndOrder(lst1,lst2))
