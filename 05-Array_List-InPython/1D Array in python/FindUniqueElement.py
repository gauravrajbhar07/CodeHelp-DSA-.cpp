#  i/p
#  11
#  1 2 4 2 1 3 6 5 5 6 4

#  o/p
#  3

def FindUniqueElement(arr):
    ans = 0
    for i in arr:
        ans = ans^i
    
    return ans

arr = [1,2 ,4 ,2, 1, 3, 6, 5, 5, 6, 4]
dublicate = FindUniqueElement(arr)
print(dublicate)