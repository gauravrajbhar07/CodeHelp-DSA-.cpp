

# Input : 
# lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
# lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
# Output :
# [9, 10, 4, 5]


def InterSection(arr,brr):

    # //set using due to avoid unique values 

    lst1 = set(arr)
    # print(lst1)
    lst2 = set(brr)
    # print(lst2)
    
    ans = []

    for i in lst1:
        if(i in lst2):
            
            ans.append(i)
        
    
    return ans



lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]

res = InterSection(lst1,lst2)
print(res)