# Sort an array of 0s, 1s and 2s



def DutchNationalFlagProblems(arr):


    low = 0
    mid = 0 
    high = len(arr) - 1

    while(mid <= high):
        # print("hllo")
        if(arr[mid] == 0):
            arr[low],arr[mid] = arr[mid],arr[low]
            
            mid = mid + 1
            low = low + 1

        elif(arr[mid] == 1):
            mid = mid + 1

        else:
            arr[mid],arr[high] = arr[high],arr[mid]
            high = high -1 

    for i in arr:
        print(i,end=" ")


arr = [0, 1, 2, 0, 1, 2]


brr=[0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
# 0 0 0 0 0 1 1 1 1 1 2 2

DutchNationalFlagProblems(brr)