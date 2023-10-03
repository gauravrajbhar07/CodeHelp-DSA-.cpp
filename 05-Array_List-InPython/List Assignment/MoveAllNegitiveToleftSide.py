def moveNegLeft(arr):
    length  = len(arr)
    left = 0
    right = length - 1
     
    
    while(left <= right ):
        
        if(arr[left] < 0 and arr[right] < 0):
            left+=1
            
        elif(arr[left] < 0 and arr[right] > 0):
            left+=1
            right-=1
            
        elif(arr[left] > 0 and arr[right] < 0):
            arr[left],arr[right] = arr[right],arr[left]
            right-=1
        else:
            left+=1
            right+=1
            
    return arr
    
    
        
arr= [-12, 11, -13, -5, 6, -7, 5, -3, -6]
# output 
# [-12, -6, -13, -5, -3, -7, 5, 6, 11] 
print(moveNegLeft(arr))
    