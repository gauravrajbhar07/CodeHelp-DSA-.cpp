def printExtrimes(arr):

    left = 0
    right = len(arr) - 1

    while(True):

        if(left > right):
            break
        elif(left == right):
            # print("hel")
            print(arr[left],end='')
        else:

            print(arr[left],arr[right],end=' ')


        left = left + 1
        right = right - 1
        


# list 
arr = [2,3,5,6,7,8]
printExtrimes(arr)

# for i in arr:
#     print(i)
